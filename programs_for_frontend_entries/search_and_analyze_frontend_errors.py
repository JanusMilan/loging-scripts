import re
import sys 
from enum import Enum
from known_frontend_errors import FrontendErrors


known_frontend_errors = FrontendErrors.known_frontend_errors


class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    search_error = 1
    found_error = 2   
    

def prepare_string_for_regex(string):  
    """ for prepare of the strings for the regex syntax
        :param: string: string to prepare
    """
    string = string.replace("[", "\[") 
    string = string.replace("]", "\]") 
    string = string.replace("(", "\(") 
    string = string.replace(")", "\)") 
    string = string.replace("\"", "\\\"")    
    string = string.replace('$', '\$')
    return string


def analyze_error(infile):  
    """ for analyzing the monthly errors: Assign errors to error group and error type
        :param: infile:  
    """       
    with open(infile, 'r') as file: 
        for line in file:
            machine_state = MachineState.search_error
            error_line = re.split('::',line)               
            line_pattern = r".*(\[\[ERR \]\] \[\[TIME\]\] .* msec:|\[\[ERR \]\]).*"
            for error_group,group_value  in known_frontend_errors.items():     
                for error_subgroup in group_value:                      
                    if re.match(line_pattern + error_group + error_subgroup, error_line[1]) is not None:   
                        known_frontend_errors[error_group][error_subgroup].append(int(error_line[0]))   
                        machine_state = MachineState.found_error                       
                        break
                    else:                                 
                        machine_state = MachineState.search_error
                        continue
                if  machine_state == MachineState.found_error:
                    break
                if machine_state == MachineState.search_error:
                    continue
                else:
                    raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))
            if machine_state == MachineState.search_error:           
                error_group = "NEW ERROR TYPE: "           
                error_subgroup = prepare_string_for_regex(error_line[1].rstrip()) 
                if "\[\[ERR \]\] \[\[TIME\]\]" in error_subgroup:
                    error_subgroup = re.split("\d{0,} msec: ", error_subgroup)
                else:    
                    if ": \[\[ERR \]\] " in error_subgroup: 
                       error_subgroup = error_subgroup.split(": \[\[ERR \]\] ")        
                    else:
                        continue
                if re.match(line_pattern, error_line[1]) is not None:
                    if known_frontend_errors[error_group].get(error_subgroup[1]) is None:                    
                        known_frontend_errors[error_group].update({error_subgroup[1] : []})  
                        known_frontend_errors[error_group][error_subgroup[1]].append(int(error_line[0]))
                    else:
                        known_frontend_errors[error_group][error_subgroup[1]].append(int(error_line[0]))   
                else:
                    continue
            elif machine_state == MachineState.found_error:
                continue
            else:
                raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))     
                    
                    
def write_output_file(outfile):    
    """ for formating of output and for output of frontend errors into outputfile
        :param: outfile: output file for the evalation data
    """                 
    with open(outfile, 'w+') as file: 
        for error_group,value  in known_frontend_errors.items():
            for error_subgroup in value:                
                number_of_errors = len(known_frontend_errors[error_group][error_subgroup])
                if 0 < number_of_errors < 10:
                    file.write(error_group +  error_subgroup  + str(known_frontend_errors[error_group][error_subgroup]) + '\n') 
                elif number_of_errors  >= 10:                                    
                    file.write(error_group +  error_subgroup  + ": [number of errors: " + str(number_of_errors) + ']\n')  
                else:
                    continue

    
def main():
    """ main function serves for process control     
    """
    infile = ""    
    outfile = ""
    try:
        infile = sys.argv[1]
    except IndexError:
        sys.exit( "input file parameter missing")
    try:
        outfile = sys.argv[2]
    except IndexError:
        sys.exit("output file parameter missing")
    analyze_error(infile)
    write_output_file(outfile)    
    

if __name__ == "__main__":
    main()        