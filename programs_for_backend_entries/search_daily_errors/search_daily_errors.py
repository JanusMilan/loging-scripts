import re
import sys
from enum import Enum


class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    wait_for_server_start = 1
    wait_for_next_server_start = 2
    wait_for_error_rest = 3       
    no_error_rest = 4     

    
def search_error_entries(input_file, output_file, day_to_check_errors):
    """ search for error entries in desired file between two server starts
    :param: input_file: .log file with data to  evaluate
    :param: output_file: output file for the evalation data
    :param: day_to_check_errors: day of server start from when the errors are searched until the next server start
    """
    to_ignore = "DbcKeyExceptionMapper"
    machine_state = MachineState.wait_for_server_start
    status_error_rest = MachineState.no_error_rest 
    outfile = open(output_file, 'a+')
    with open(input_file, 'r') as infile:
        for row in infile: 
            server_start = re.search(r"server started at http://0.0.0.0:1999" , row)
            date_of_entry = re.match(r"\d{4}-\d{2}-(\d{2}) \d{2}:\d{2}", row)
            if  machine_state == MachineState.wait_for_server_start:            
                if  date_of_entry is not None and date_of_entry[1] ==  day_to_check_errors:
                        if  server_start  is not None:
                            machine_state = MachineState.wait_for_next_server_start
                            outfile.write(row)
                            continue
                        else:
                           continue
                else:
                   continue
            elif  machine_state == MachineState.wait_for_next_server_start:
                if server_start is None:
                    if date_of_entry is not None: 
                        if re.search(r" ERROR ",  row) is not None and  re.search(to_ignore,  row) is None:
                            status_error_rest =  MachineState.wait_for_error_rest                             
                            outfile.write(row)
                            continue
                        else:
                            status_error_rest = MachineState.no_error_rest  
                            continue                        
                    else:
                        if  status_error_rest == MachineState.wait_for_error_rest:                   
                            outfile.write(row)
                            continue
                        else: 
                            continue
                else: 
                    outfile.write(row)
                    break
            else:
                raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))    
    outfile.close()
    
    
 

def main():
    """ main function """
    infile = ""
    outfile = ""
    day_to_check_errors = ""
    try:
        infile = sys.argv[1]
    except IndexError:
        sys.exit( "input file parameter missing")
    try:
        outfile = sys.argv[2]
    except IndexError:
        sys.exit("output file parameter missing")
    try:
        day_to_check_errors = sys.argv[3]
    except IndexError:
        sys.exit("day to check parameter missing") 

    # infile = "test_input_daily-errors.txt"
    # outfile = "test_output_daily-errors.txt"
    # day_to_check_errors = "01"

    search_error_entries(infile, outfile, day_to_check_errors)
 
if __name__ == "__main__":
    main()