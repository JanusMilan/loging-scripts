import re

def get_number_loaded_programs_message(prog_load_number, message):    
    if len(prog_load_number) == 0: 
        return message + 'ERROR: missing number of load programs ' 
    elif len(prog_load_number) < 6:
        return message + 'WARNING: number of load programs is to low ' 
    else:
        return message + 'INFO: loaded ' + prog_load_number + ' programs'   
    
def create_log_message_entry(server_start_entry, prog_load_entry):          
    #  'prog_load_entry' match to 'server_start_entry' IS NOT found
    if prog_load_entry == 'missing':        
        message = 'ERROR: server started at: ' + server_start_entry[0] + ' an programs are not loaded'
    else:            
        # 'prog load entry' match to 'server start entry' found AND server start time IS correct
        if ( server_start_entry[0] == prog_load_entry[0] ) and ( server_start_entry[1]  == '03:00' ):
            message = get_number_loaded_programs_message(prog_load_entry[2]  ,'INFO: server started at: ' + server_start_entry[0] + ' and ') 
        #  'prog load entry' match to 'server start entry' found AND server start time IS NOT correct   
        elif ( server_start_entry[0] == prog_load_entry[0] ) and  ( server_start_entry[1]  != '03:00' ):
            message = get_number_loaded_programs_message( prog_load_entry[2] , 'ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + ' and ')  
        #  'prog load entry' NOT match to 'server start entry' found AND server start time IS correct   
        elif ( server_start_entry[0] != prog_load_entry[0] ) and  ( server_start_entry[1]  == '03:00' ):
            message = 'ERROR: server started at: ' + server_start_entry[0] + ' and programs are not loaded'
        else:
            message =  'ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + ' and programs are not loaded'           
    with open('output.log', 'a+') as output: 
        output.write(message + "\n")            

def get_date_hour_min(zeile):    
    date_hour_min = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", zeile)
    return [ date_hour_min.group(), date_hour_min.group(1) ]
    
def get_server_start_line(zeile):    
    if re.search(r"server started at http://0.0.0.0:1999" , zeile)  is not None:
        date_hour_min = get_date_hour_min(zeile) 
        return [ date_hour_min[0],  date_hour_min[1] ]
    else:
        return None     
        
def get_number_load_programs_line(zeile):    
    prog_load_number =  re.findall(r"\[(\d{1,})\]", zeile)
    if len(prog_load_number) == 0:
        prog_load_number = ''
    else:
        prog_load_number =  prog_load_number[0] 
    if  len( re.findall(r"Number of programs stored in the database", zeile) ) > 0:  
        date_hour_min = get_date_hour_min(zeile) 
        return [ date_hour_min[0],  date_hour_min[1], prog_load_number]
    else:
        return None            
        
def state_machine():
    status_server_start = "wait"
    status_prog_load = "wait"
    counter = 0
    with open('ausgabe.log', 'r') as eingabe:             
        for zeile in eingabe:
            if  status_server_start != "run":             
                server_start_line = get_server_start_line(zeile)   
                # found .. 'server start ..' entry
                if  server_start_line  is not None:    
                    status_server_start = "run"
                    continue
            # search '.. programs stored ..' entry         
            if  status_server_start == "run"  and status_prog_load == "wait": 
                if counter < 4:
                    counter = counter + 1
                    number_load_programs_line = get_number_load_programs_line(zeile)
                    # found '.. programs stored ..' entry
                    if  number_load_programs_line is not None: 
                        create_log_message_entry(server_start_line, number_load_programs_line)
                        status_server_start = "wait"
                        status_prog_load = "wait"
                        counter = 0
                        continue
                # entry '.. programs stored ..' NOT found        
                else:
                    create_log_message_entry(server_start_line, "missing")
                    status_server_start = "wait"
                    status_prog_load = "wait"
                    counter = 0                           
                    continue        
                    
def main():
    state_machine()

if __name__ == "__main__":
    main()


        
        
        
        
        
        

