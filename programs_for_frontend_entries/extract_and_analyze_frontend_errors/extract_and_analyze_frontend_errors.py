import re
import sys 
from enum import Enum
from known_frontend_errors import FrontendErrors
from copy import deepcopy


class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    search_error = 1
    found_error = 2      


def prepare_string_for_regex(string):  
    """ for prepare of the strings for the regex syntax for processes of filtering
        :param: string: string to prepare
    """
    string = string.replace("[", "\[") 
    string = string.replace("]", "\]") 
    string = string.replace("(", "\(") 
    string = string.replace(")", "\)") 
    string = string.replace("\"", "\\\"")    
    string = string.replace('$', '\$')
    return string
    

def remove_regex_escapes(string):  
    """ for removing regex escapes out of the strings for the output
        :param: string: string to process
    """
    string = string.replace("\[", "[") 
    string = string.replace("\]", "]")     
    string = string.replace("\(", "(") 
    string = string.replace("\)", ")") 
    string = string.replace("\\\"", "\"")    
    string = string.replace('\$', '$')
    string = string.replace('.*', '')
    return string        
   

def compile_regex_dict(known_frontend_errors_copy):  
    """ for constructing of dictionary with compiled regexes of known frontend errors as value
   :param: known_frontend_errors_copy: deepcopy of dictionary "known_frontend_errors"
    """   
    line_pattern = r".*(\[\[ERR \]\] \[\[TIME\]\] .* msec:|\[\[ERR \]\]).*"
    for error_group,group_value  in known_frontend_errors_copy.items():     
        for error_subgroup, values in group_value.items():      
            known_frontend_errors_copy[error_group][error_subgroup] = re.compile(line_pattern + error_group + error_subgroup)               
    return known_frontend_errors_copy       
 
 
def search_known_error(known_frontend_errors, client_logger_error_regex_dict, line):  
    """ for analyzing at this time known monthly errors: 
   - registers the line where the error type is occurred, if line contain known error
   :param: known_frontend_errors: dictionary of the errors, which are already registered
   :client_logger_error_regex_dict:  dictionary with compiled regexes of monthly frontend errors, which are already registered in dictionary  "known_frontend_errors"
   :line: actual line of the input file to be processed
    """   
    machine_state = MachineState.search_error
    for error_group,group_value  in known_frontend_errors.items():     
        for error_subgroup, values in group_value.items():    
            regex = client_logger_error_regex_dict[error_group][error_subgroup]
            if regex.match(line[1]) is not None:     
                known_frontend_errors[error_group][error_subgroup].append(int(line[0]))
                machine_state = MachineState.found_error                       
                return MachineState.found_error
            else:
                continue
    if machine_state == MachineState.search_error:
        return MachineState.search_error
    else:
        raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))


def search_unknown_error(known_frontend_errors, client_logger_error_regex_dict, line):
    """ for analyzing at this time unknown monthly errors: 
    - extends the dictionary  "known_frontend_errors" with new error type, if line contain unknown error for the first time 
    - registers the line where the new error type is occurred
   :param: known_frontend_errors: dictionary with the errors, which are already registered
   :client_logger_error_regex_dict:  dictionary of compiled regexes of monthly frontend errors, which are already registered in dictionary  "known_frontend_errors"
   :line: actual line of the input file to be processed
    """   
    error_group = "NEW ERROR TYPE: "      
    error_subgroup_regex = prepare_string_for_regex(line[1].rstrip()) 
    if ": \[\[ERR \]\] \[\[TIME\]\]" in error_subgroup_regex:              
        error_subgroup_regex = re.split("\d{0,} msec: ", error_subgroup_regex) 
    elif ": \[\[ERR \]\]" in error_subgroup_regex: 
           error_subgroup_regex = error_subgroup_regex.split(": \[\[ERR \]\] ")  
    else:
        return MachineState.search_error              
    if known_frontend_errors[error_group].get(error_subgroup_regex[1]) is None:    
        known_frontend_errors[error_group].update({error_subgroup_regex[1] : []})  
        known_frontend_errors[error_group][error_subgroup_regex[1]].append(int(line[0]))
    else:     
        known_frontend_errors[error_group][error_subgroup_regex[1]].append(int(line[0]))   
    return MachineState.found_error   


def filter_error_lines(infile, known_frontend_errors):  
    """ for analyzing the monthly frontend errors: 
    - read all log lines from a infile
    - regulates the filtering of the data by distributing the lines of file on two functions
    - the known errors are processed by function "search_known_error"
    - the unknown errors are processed by function "search_unknown_error"
    :param: infile:  file which is generated by the program "extract_monthly_frontend_entries.py"
    :param: known_frontend_errors: dictionary of the errors, which are already registered
    """               
    client_logger_error_regex_dict = compile_regex_dict(deepcopy(known_frontend_errors))             
    with open(infile, 'r') as file:         
        for line in file:
            machine_state = MachineState.search_error
            line = re.split('::',line)        
            machine_state = search_known_error(known_frontend_errors, client_logger_error_regex_dict, line)
            if machine_state == MachineState.found_error:      
                continue
            elif machine_state == MachineState.search_error:     
                machine_state = search_unknown_error(known_frontend_errors, client_logger_error_regex_dict, line) 
                if machine_state == MachineState.found_error:   
                    client_logger_error_regex_dict = compile_regex_dict(deepcopy(known_frontend_errors)) 
                elif  machine_state == MachineState.search_error:
                    continue
                else:
                    raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))                      
            else:
                raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))     
                        
                    
def write_output_file(outfile, known_frontend_errors):    
    """ for formating and for creating of the output file
        :param: outfile: output file for the evalation data
        :param: known_frontend_errors: dictionary of the errors, which are already registered
    """                 
    with open(outfile, 'w+') as output_file: 
        for error_group,value  in known_frontend_errors.items():
            output_file.write(remove_regex_escapes(error_group) + '\n')            
            for error_subgroup in value:                
                number_of_errors = len(known_frontend_errors[error_group][error_subgroup])
                if 0 < number_of_errors < 10:   
                    all_error_appearances = str(known_frontend_errors[error_group][error_subgroup])
                    output_file.write('{:10s} {:s} {:s}\n'.format(" ", remove_regex_escapes(error_subgroup), all_error_appearances))                    
                elif number_of_errors  >= 10:                                    
                    first_error_appearance = known_frontend_errors[error_group][error_subgroup][0]
                    output_file.write('{:10s} {:s} {:s} {:d} {:s} {:d}{:s}\n'.format(" ", remove_regex_escapes(error_subgroup), ": [number of errors:", number_of_errors, ", first error appearance:", first_error_appearance, "]"))                       
                else:
                    continue         
    
def main():
    """ main function serves for process control    
    """    
    try:
        filter_error_lines(sys.argv[1],  FrontendErrors.known_frontend_errors) 
        write_output_file(sys.argv[2], FrontendErrors.known_frontend_errors)
    except IndexError:
        sys.exit("usage: extract_monthly_frontend_entries <infile> <outfile>") 

if __name__ == "__main__":
    main()        