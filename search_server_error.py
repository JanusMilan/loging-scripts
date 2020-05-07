import re
import sys
from enum import Enum
 

error_has_occurred = False
""" Variable contains status whether errors occurred this month """


def check_if_scheduled(start_time):
    """ Evaluates if server start is scheduled """
    scheduled_starts = ['03:00' , '03:01' , '03:02' , '03:03'] 
    return start_time in scheduled_starts


def evaluate_server_start_entry(start_date, start_time, number_of_programs, outfile):
    """ Evaluates the server start messages
    :param: start_date: date of server start 
    :param: start_time: hour and min of server start
    :param: number_of_programs: data with number of programs
    :param: outfile: file for output of evaluation
    """
    global error_has_occurred
    scheduled_start = 'start at: '
    un_scheduled_start = 'ERROR: unscheduled start at: '
    programs_occurs = '; programs : '
    programs_dont_occurs =  ' ERROR:  no programs \n'
    with open(outfile, 'a+') as file:
        if check_if_scheduled(start_time):
            if number_of_programs == None:
                error_has_occurred = error_has_occurred or True
                file.write(scheduled_start + start_date + programs_dont_occurs)
            else:
                file.write(scheduled_start + start_date +  programs_occurs + number_of_programs + '\n')              
        else:
            if number_of_programs == None:
                error_has_occurred = error_has_occurred or True
                file.write(un_scheduled_start + start_date + programs_dont_occurs)
            else:
                file.write(un_scheduled_start + start_date +  programs_occurs + number_of_programs + '\n')
                error_has_occurred = error_has_occurred or True


class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    wait_for_server = 1
    wait_for_programs = 2


def search_server_start_entry(log_file, outfile):
    """ Searches the log file for messages "..server started at.." and "..Number of programs stored.."
    :param: log_file: file to be evaluate
    :param: outfile: file for output of evaluation
    """
    machine_state  = MachineState.wait_for_server
    row_counter = 0
    with open(log_file, 'r') as file:
        for row in file:
            if  machine_state == MachineState.wait_for_server:
                if re.search(r"server started at http://0.0.0.0:1999" , row)  is not None:
                    date_of_entry = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", row)
                    machine_state = MachineState.wait_for_programs
                    row_counter = 0
                    continue
                else:
                    continue
            elif  machine_state == MachineState.wait_for_programs:
                if row_counter < 4:
                    row_counter = row_counter + 1
                    programs_entry = re.search(r"Number of programs stored in the database: \[(\d{1,})\]", row)               
                    if  programs_entry is not None:
                        evaluate_server_start_entry(date_of_entry[0], date_of_entry[1], programs_entry[1], outfile)
                        machine_state = MachineState.wait_for_server
                        continue
                    else:
                        continue
                else:
                    evaluate_server_start_entry(date_of_entry[0], date_of_entry[1],  None, outfile)
                    machine_state = MachineState.wait_for_server
            else:
                raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))


def evaluate_monthly_errors(outfile):
    """ Evaluates whether errors occurred this month """
    if error_has_occurred != True:
        with open(outfile, 'a+') as output_file:
            output_file.write('\n all server starts are regular' + "\n")
    else:
        with open(outfile, 'a+') as output_file:
            output_file.write('\n errors occurred this month' + "\n")


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
    search_server_start_entry(infile, outfile)
    evaluate_monthly_errors(outfile)

if __name__ == "__main__":
    main()