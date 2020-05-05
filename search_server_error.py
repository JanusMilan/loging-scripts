import re
import sys
            
def check_if_sheduled(start_time):
    """ Evaluates if server start is  sheduled """
    sheduled_starts = ['03:00' , '03:01' , '03:02' , '03:03']
    return start_time in sheduled_starts

def evaluate_server_start_entry(start_date, start_time, number_of_programs):    
    """ Evaluates the server start messages """
    sheduled_start = 'server started at: ' 
    un_sheduled_start = 'server started UNSHEDULED at: '
    programs_occurs = '; with number of programs entry' 
    programs_dont_occurs =  ': ERROR no number of programs entry'    
    if check_if_sheduled(start_time):     
        if number_of_programs == "None":
            return sheduled_start + start_date + programs_dont_occurs
        else:
            return sheduled_start + start_date +  programs_occurs + number_of_programs               
    else:
        if number_of_programs == "None":
            return un_sheduled_start + start_date + programs_dont_occurs      
        else:
            return un_sheduled_start + start_date +  programs_occurs + number_of_programs
  
def search_server_start_entry(log_file):
    """ Searches the log file for messages "..server started at.." and "..Number of programs stored.."   """
    status_machine  = "wait for server start"
    server_start_date = ""
    programs_counter = 0
    server_start_list = list() 
    with open(log_file, 'r') as file:             
        for row in file:
            date_of_entry = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", row)
            if  status_machine == "wait for server start":
                if  re.search(r"server started at http://0.0.0.0:1999" , row)  is not None:
                    server_start_date = date_of_entry[0]
                    server_start_time = date_of_entry[1]
                    status_machine = "wait for programs" 
                    programs_counter = 0
                    continue
            if  status_machine == "wait for programs":
                if programs_counter < 4:
                    programs_counter = programs_counter + 1
                    programs_entry = re.search(r"Number of programs stored in the database: \[(\d{1,})\]", row)                    
                    if  programs_entry is not None: 
                        number_of_programs = programs_entry[1]
                        enty_to_evaluate = evaluate_server_start_entry(server_start_date, server_start_time, number_of_programs)
                        server_start_list.append(enty_to_evaluate)
                        status_machine = "wait for server start"
                else:
                    enty_to_evaluate = evaluate_server_start_entry(server_start_date, server_start_time,  "None")
                    server_start_list.append(enty_to_evaluate)
                    status_machine = "wait for server start"
    return server_start_list

def evaluate_server_starts(server_start_list, outfile):      
    """ Evaluates whether all server starts are regular """
    error_list = list()
    status_error_server_start = "no server start error"
    for row in server_start_list:
         if re.search(r"ERROR", row)  is not None:
            status_error_server_start = "server start error occurs"   
            start_date = re.search(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", row)[0]
            error_list. append(start_date)                       
    if status_error_server_start == "server start error occurs":
        server_start_list.append("errors occurs on:")        
        for element in error_list:
            server_start_list.append("-> " + element) 
    else:
           server_start_list.append('all server starts are regular' + "\n")  
    return server_start_list
    
def main():
    month_to_check = ""
    outfile = ""
    if len(sys.argv) == 3:
        month_to_check = sys.argv[1]
        outfile = sys.argv[2]
    else:
       month_to_check = input("please enter input file (month.log) to check: ")  
       outfile = input("please enter output file name: ")
    server_start_list = search_server_start_entry(month_to_check)
    output_list = evaluate_server_starts(server_start_list, outfile)    
    with open(outfile, 'w') as outfile:
        for element in output_list:
            outfile.write(element + "\n")
            
if __name__ == "__main__":
    main()