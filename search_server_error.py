import re
import os
import datetime
import sys

def evaluate_server_start_entry(server_start_entry, prog_load_entry):
    """ Evaluates the messages "..server started at.." and "..Number of programs stored.." 
    and writes evaluation into the output file
    """
    with open('output.log', 'a+') as output_file:
        if prog_load_entry != " entry ..programs are loaded.. is missing" and server_start_entry[1] == '03:00':
            output_file.write('INFO: server started at: ' + server_start_entry[0] + ';  INFO: loaded ' + prog_load_entry[1] + ' programs' + "\n")
        elif prog_load_entry != " entry ..programs are loaded.. is missing"and server_start_entry[1]  != '03:00':
            output_file.write('ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + '; INFO: loaded ' + prog_load_entry[1] + ' programs' + "\n")
        elif prog_load_entry == " entry ..programs are loaded.. is missing" and server_start_entry[1] == '03:00':
            output_file.write('INFO: server started at: ' + server_start_entry[0] + ': ERROR programs are not loaded' + "\n")
        else:
            output_file.write('ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + ': ERROR programs are not loaded' + "\n")


def search_server_start_entry(current_log_file: str):
    """ Searches the log file for messages "..server started at.." and "..Number of programs stored.."   
    and gives both reports to the "evaluate_server_start_entry" Function to continue the evaluation
    :param: current_log_file: current month log file 
    :type current_log_file: string    
    """
    status_server_start : str = "wait for server start"
    counter = 0
    with open(current_log_file, 'r') as input_file:             
        for row in input_file:
            date_of_entry = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", row)
            if  status_server_start == "wait for server start":
                if  re.search(r"server started at http://0.0.0.0:1999" , row)  is not None:
                    status_server_start =  [date_of_entry[0],  date_of_entry[1]]
                    continue
            if  status_server_start != "wait for server start":
                if counter < 4:
                    counter = counter + 1
                    if  len( re.findall(r"Number of programs stored in the database", row) ) > 0: 
                        evaluate_server_start_entry(status_server_start, [ date_of_entry[0] , re.findall(r"\[(\d{1,})\]", row)[0]])
                        status_server_start = "wait for server start"
                        counter = 0
                else:
                    evaluate_server_start_entry(status_server_start, " entry ..programs are loaded.. is missing")
                    status_server_start = "wait for server start"
                    counter = 0


def evaluate_server_starts():      
    """ Evaluates the evaluation of the log file, whether all server starts are regular
    and appends evaluation to the output file
    """
    list_of_errors = list()
    status_error_server_start = "no server start error"
    with open('output.log', 'r') as input_file:
        for row in input_file:
             if re.search(r"ERROR", row)  is not None:
                status_error_server_start = "server start error occurs"
                list_of_errors. append(re.search(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", row)[0])
    if status_error_server_start == "server start error occurs":
        with open('output.log', 'a+') as input_file:
            input_file.write('server start error occurs on' + "\n")
            for element in list_of_errors:
                input_file.write("--> " + element + "\n") 
    else:
       with open('output.log', 'a+') as input_file:
           input_file.write('all server starts are regular' + "\n")  


def find_current_log_file() -> str:      
    """ search the current log file
    :warnings: make exit() in case of failing to find current log file
    :return: returns current log file
    :rtype: string
    """
    now = datetime.datetime.now()
    log_file = ""
    if now.month < 10:
        current_log_file = "0" + str(now.month) + ".log"
    else: 
        current_log_file = str(now.month) + ".log"

    file_list = os.listdir(".")   
    current_log_file_status : str = " search current log file"
    for filename in file_list: 
        if filename == current_log_file:
            return current_log_file
    if  current_log_file_status == " search current log file":        
        sys.exit('Error!') 


def main():
    search_server_start_entry(find_current_log_file())
    # print(search_server_start_entry.__annotations__)  
    evaluate_server_starts()
    # print(find_current_log_file.__doc__)
    # print(find_current_log_file.__annotations__)  
    

if __name__ == "__main__":
    main()