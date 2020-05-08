import re
import sys
from enum import Enum


class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    wait_for_error = 1
    wait_for_rest_of_error = 2


def search_compiler_error_errors(infile, outfile):
    """ search cross-compiler errors 
    :param: infile: .log file with data to  evaluate 
    :param: outfile: output file for the evalation data
    """
    machine_state = MachineState.wait_for_error
    output_file = open(outfile, 'a+')
    with open(infile, 'r') as file: 
        for row in file:
            compiler_error = re.search(r"d.f.i.r.c.AbstractCompilerWorkflow", row)
            not_rest_of_error = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", row)
            if  machine_state == MachineState.wait_for_error:     
                if compiler_error is not None:
                    output_file.write("========== NEXT Cross-Compiler ERROR ========== \n")
                    output_file.write(row)
                    machine_state = MachineState.wait_for_rest_of_error             
                    continue
                else:
                    continue
            elif machine_state == MachineState.wait_for_rest_of_error:         
                if not_rest_of_error is None:
                    output_file.write(row)
                    continue
                else:
                    machine_state = MachineState.wait_for_error
                    continue
            else:
                raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))
    output_file.close()


def main():
    """ main function serves for process control """
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
    search_compiler_error_errors(infile, outfile)    

if __name__ == "__main__":
    main()        