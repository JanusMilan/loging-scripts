import re
import sys
from enum import Enum

class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    wait_for_server_start = 1
    wait_for_next_server_start = 2       

def search_error_entries(input_file, day_to_check, output_file):
    """ search for error entries in desired file
 
    :param: 
    :param: 
    """   
    status_server_start = MachineState.wait_for_server_start
    output_file = open(output_file, 'a+')    
    with open(input_file, 'r') as input_file:            
        for element in input_file:                        
            server_start = re.search(r"server started at http://0.0.0.0:1999" , element)
            if  status_server_start == MachineState.wait_for_server_start:
                date_of_entry = re.match(r"\d{4}-\d{2}-(\d{2}) \d{2}:\d{2}", element)
                if  date_of_entry[1] ==  day_to_check:
                        if  server_start  is not None:
                            status_server_start = MachineState.wait_for_next_server_start
                            output_file.write(element)
                            continue
                        else:
                           continue
                else:
                   continue
            elif  status_server_start == MachineState.wait_for_next_server_start:
                if server_start is None:
                    if date_of_entry is not None and re.search(r"ERROR",  element) is not None:      
                        output_file.write(element)
                        continue
                    else:
                        continue
                else: # zweiten server start aufnehmen
                    output_file.write(element)
                    break
            else:
                raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(status_server_start))        
    output_file.close()

def main():
    """ main function """  
    input_file = "04.log"
    output_file = "TEST.txt"
    day_to_check = "01"    
    search_error_entries(input_file , day_to_check, output_file)
    
if __name__ == "__main__":
    main()