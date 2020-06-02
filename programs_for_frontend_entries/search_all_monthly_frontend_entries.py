import re
import sys
from enum import Enum


""" list with entries to ignore """
entries_to_ignore =  [
        ".*jsToAppInterface >invalid webview type caused by: \[object Object\]",
        ".*init .* view",
        ".*init .* delete"
]


""" list with compiled pattern of entries to ignore """
pattern_entries_to_ignore = []
for element in entries_to_ignore:
    pattern_entries_to_ignore.append(re.compile(element))
    
    
class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    search_entry_to_ignore = 1
    found_entry_to_ignore = 2   
    

def search_client_logger_entries(infile, outfile):
    """ for searching of all monthly frontend entries and noting their line numbers
    :param: infile: .log file with data to  evaluate 
    :param: outfile: output file for the evalation data
    """
    output_file = open(outfile, 'x')
    with open(infile, 'r') as file:  
        for line_number,line in enumerate(file):
            line_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*(INFO d.fhg.iais.roberta.util.ClientLogger - log entry: (\[\[ERR \]\] \[\[TIME\]\] .* msec:|\[\[TIME\]\] .* msec:|\[\[ERR \]\]|\[\[INFO\]\])) (.*)"
            client_logger_line = re.compile(line_pattern).match(line)           
            if client_logger_line is not None:
                machine_state = MachineState.search_entry_to_ignore
                for pattern in pattern_entries_to_ignore: 
                    relevant_client_logger_line = pattern.match(line)
                    if relevant_client_logger_line is None:     
                        continue
                    else:
                        machine_state = MachineState.found_entry_to_ignore
                        break
                if machine_state == MachineState.found_entry_to_ignore: 
                    continue
                else:                    
                    output_file.write(str(line_number + 1) + "::" + client_logger_line[1]  + ": " + client_logger_line[2]  + " " + client_logger_line[4] + "\n")
            else:
                continue
    output_file.close() 
    
    
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
    search_client_logger_entries(infile, outfile)    


if __name__ == "__main__":
    main()        