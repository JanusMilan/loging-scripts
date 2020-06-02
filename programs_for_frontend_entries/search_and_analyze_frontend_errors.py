import re
import sys 
from enum import Enum
from known_frontend_errors import FrontendErrors

known_frontend_errors = FrontendErrors.known_frontend_errors
# __init__.py
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
            error = re.split('::',line)   
            for error_group,group_value  in known_frontend_errors.items(): 
                for error_type,value in group_value.items():                      
                    if re.match(error_group + error_type, error[1]) is not None:   
                        known_frontend_errors[error_group][error_type].append(int(error[0]))   
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
                error_type = prepare_string_for_regex(error[1].rstrip())                
                if known_frontend_errors[error_group].get(error_type) is None:
                    known_frontend_errors[error_group].update({error_type : []})  
                    known_frontend_errors[error_group][error_type].append(int(error[0]))
                else:
                    known_frontend_errors[error_group][error_type].append(int(error[0]))                              
            elif machine_state == MachineState.found_error:
                continue
            else:
                raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))     
                    
def write_output_file(outfile):    
    """ for formating of output and for output into outputfile
        :param: outfile: output file for the evalation data
    """                 
    with open(outfile, 'w+') as file: 
        for error_group,value  in known_frontend_errors.items():
            for error, error_enumeration in value.items():    
                number_of_errors = len(known_frontend_errors[error_group][error])
                if  number_of_errors < 5:
                    file.write(error_group +  error  + str(known_frontend_errors[error_group][error]) + '\n') 
                else:
                    file.write(error_group +  error  + ": [number of errors: " + str(number_of_errors) + ']\n')       
                
def main():
    """ main function serves for process control 
    how to run program: python3 search_and_analyze_frontend_errors.py test_infile_frontende_error.txt test_outfile_frontende_error.txt    
    """
    infile = "front_end_error_file.txt"    
    outfile = "TEST.txt"
    # try:
        # infile = sys.argv[1]
    # except IndexError:
        # sys.exit( "input file parameter missing")
    # try:
        # outfile = sys.argv[2]
    # except IndexError:
        # sys.exit("output file parameter missing")
    analyze_error(infile)
    write_output_file(outfile)    
    

if __name__ == "__main__":
    main()        