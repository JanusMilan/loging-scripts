import re
import sys 
from enum import Enum
from known_backend_errors import BackendErrors


class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    search_error = 1
    found_error = 2      


def prepare_string_for_regex(string):  
    """ for prepare of the strings for the regex-syntax for processes of filtering
        :param: string: string to prepare for regex-syntax for the purpose of compiling of regex
    """
    string = string.replace("[", "\[") 
    string = string.replace("]", "\]") 
    string = string.replace("{", "\{") 
    string = string.replace("}", "\}")     
    string = string.replace("(", "\(") 
    string = string.replace(")", "\)") 
    string = string.replace("\"", "\\\"")    
    string = string.replace('$', '\$')
    return string
    

def remove_regex_escapes(string):  
    """ for removing regex escapes out of the strings for the output
        :param: string: string to process for the purpose of the output
    """
    string = string.replace("\[", "[") 
    string = string.replace("\]", "]")   
    string = string.replace("\{", "{") 
    string = string.replace("\}", "}")       
    string = string.replace("\(", "(") 
    string = string.replace("\)", ")") 
    string = string.replace("\\\"", "\"")    
    string = string.replace('\$', '$')
    string = string.replace('.*', '')
    return string        
   

def compile_regex_dict(known_backend_errors):  
    """ for constructing of dictionary with compiled regexes of known frontend errors as value
   :param: known_backend_errors: dictionary of the errors, which are already registered
    """   
    for error_group, group_value  in known_backend_errors.items():     
        for error_subgroup in group_value:      
            known_backend_errors[error_group][error_subgroup].append(re.compile(error_group + error_subgroup))            
    return known_backend_errors       
 
 
def search_known_error(known_backend_errors, line_number_and_error_splited ):  
    """ for analyzing at this time known monthly errors: 
   - registers the line where the error type is occurred
   :param: known_backend_errors: dictionary of the errors, which are already registered
   :line_number_and_error_splited: actual line of the input file to be processed, splited in line_number and error part
    """   
    for error_group,group_value  in known_backend_errors.items():     
        for error_subgroup in group_value:            
            if known_backend_errors[error_group][error_subgroup][0].match(line_number_and_error_splited [1]) is not None:       
                known_backend_errors[error_group][error_subgroup].append(int(line_number_and_error_splited [0]))     
                return MachineState.found_error
    else:
            return MachineState.search_error
 
  
def search_unknown_error(known_backend_errors, line_number_and_error_splited ):
    """ for analyzing at this time unknown monthly errors: 
   - registers the line where the error type is occurred
   - if new error group and new error subgroup appears, function expands library by adding a new group and new  regex to the library
   - if new error subgroup appears, function expands library by adding a new subgroup and new  regex to the library   
   :param: known_backend_errors: dictionary of the errors, which are already registered
   :line_number_and_error_splited: actual line of the input file to be processed, splited in line_number and error part
    """   
    group_and_subgroup_splited = re.split(".*(ERROR .*-)( .*)", line_number_and_error_splited [1])
    line_group = prepare_string_for_regex(group_and_subgroup_splited[1])
    error_subgroup = prepare_string_for_regex(group_and_subgroup_splited[2]) 
    line_regex = re.compile(r".*(" + line_group + r")" + error_subgroup)    
    for error_group  in known_backend_errors:
        if  re.match(error_group, line_group) is not None:    
            known_backend_errors[error_group].update({error_subgroup : [line_regex,  int(line_number_and_error_splited [0])]})
            break
    else:  
            known_backend_errors.update({line_group : {error_subgroup : [line_regex, int(line_number_and_error_splited [0])]}})     
    
    
def filter_error_lines(infile, start_date, end_date, known_backend_errors):  
    """ for analyzing the monthly frontend errors in a given time interval: 
    - read all log lines from a infile
    - regulates the filtering of the data by distributing the lines of file on two functions, if one error appears
    - the known errors are distributed to function "search_known_error"
    - the unknown errors are distributed to function "search_unknown_error"
    :param: infile:  file which is generated by the program "extract_monthly_frontend_entries.py"
    :param:start_date: date from when input file is to be examined
    :param:end_date: to this point of time (date) is input file to be examined   
    :param: known_backend_errors: dictionary of the errors, which are already registered
    """     
    date_regex = re.compile(r"\d{4}-\d{2}-(\d{2}) \d{2}:\d{2}:\d{2}") 
    compile_regex_dict(known_backend_errors)  
    error_regex = re.compile(r".*(INFO d.f.i.r.p.AbstractProcessor|ERROR).*")  
    with open(infile, 'r') as input_file:           
        for line in input_file:            
            machine_state = MachineState.search_error
            date_regex_match = date_regex.search(line)
            if date_regex_match is not None:
                day_of_month = int(date_regex_match.group(1))
                if start_date <= day_of_month <= end_date:  
                    if error_regex.match(line) is not None:
                        line_number_and_error_splited  = re.split('!!!!!',line)   
                        if search_known_error(known_backend_errors, line_number_and_error_splited ) == MachineState.found_error:      
                            continue
                        elif machine_state == MachineState.search_error: 
                            search_unknown_error(known_backend_errors, line_number_and_error_splited )                  
                        else:
                            raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))     
                  
                    
def write_output_file(outfile, known_backend_errors):    
    """ for formating and for creating of the output file
        :param: outfile: output file for the evalation data
        :param: known_backend_errors: dictionary of the registered errors, which is also used for output
    """                 
    with open(outfile, 'w+') as output_file: 
        for error_group,value  in known_backend_errors.items():
            output_file.write(remove_regex_escapes(error_group) + '\n')            
            for error_subgroup in value:    
                known_backend_errors[error_group][error_subgroup].pop(0)
                number_of_errors = len(known_backend_errors[error_group][error_subgroup])                
                if 0 < number_of_errors < 10:   
                    output_file.write('{:10s} {:s} {:s}\n'.format(" ", remove_regex_escapes(str(error_subgroup)), str(known_backend_errors[error_group][error_subgroup])))                    
                elif number_of_errors  >= 10:                   
                    output_file.write('{:10s} {:s} {:s} {:d} {:s} {:d}{:s}\n'.format(" ", remove_regex_escapes(str(error_subgroup)), ": [number of errors:", number_of_errors, ", first error appearance:", known_backend_errors[error_group][error_subgroup][0], "]"))                       
                else:
                    output_file.write('{:10s} {:s}{:s}\n'.format(" ", remove_regex_escapes(str(error_subgroup)), ": [ Ø ]"))                         
  
  
def main():
    """ main function serves for process control    
    """    
    try:    
        if sys.argv[3] != "-" and sys.argv[4] != "-":
            start_date = int(sys.argv[3])
            end_date = int(sys.argv[4])
        elif sys.argv[3] == "-" and sys.argv[4] != "-":    
            start_date = 1  
            end_date = int(sys.argv[4])
        elif sys.argv[3] != "-" and sys.argv[4] == "-":                
            start_date = int(sys.argv[3])
            end_date = 31
        else:
            start_date = 1  
            end_date = 31            
        filter_error_lines(sys.argv[1], start_date, end_date,  BackendErrors.known_backend_errors) 
        write_output_file(sys.argv[2], BackendErrors.known_backend_errors)
    except IndexError:
        sys.exit("usage: extract_monthly_frontend_entries <infile> <outfile>")         


if __name__ == "__main__":
    main()        