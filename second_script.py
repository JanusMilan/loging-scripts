import re


# brauche Strings hier 
def create_log_message_entry(server_start_entry, prog_load_entry):    
    print(type(server_start_entry))
    print(server_start_entry)
    x = server_start_entry[0][0]
    y = server_start_entry[1][0]    
    print(x)
    print(y)
    if type(prog_load_entry) == str:
        print(prog_load_entry) 
    else:
        print(prog_load_entry[1][0]  )
    # with open('output.log', 'r') as output: 
        # output.write(server_start_entry.join() + server_start_entry.join() + "\n")
        # if prog_load_entry is not None:    
            # return ""
        # else:
            # return None    
            
# muss von hier Liste von Strings schicken, also matches in Strings konvertieren          
# date = server_start_date.group()
# hour_min = server_start_date.group(1) 
def get_date_hour_min(zeile):    
    date_hour_min = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", zeile) 
    if date_hour_min is not None:
        return date_hour_min
    else:
        return None 

# muss von hier Liste von Strings schicken, also matches in Strings konvertieren        
def get_server_start_line(zeile):    
    server_start_entry = re.search(r"server started at http://0.0.0.0:1999" , zeile) 
    if server_start_entry is not None:
        return [ server_start_entry, get_date_hour_min(zeile) ]
    else:
        return None             
 # muss von hier Liste von Strings schicken, also matches in Strings konvertieren     
def get_number_load_programs_line(zeile):    
    prog_load_entry = re.findall(r"Number of programs stored in the database: \[\d{6}\]", zeile)
    if  len(prog_load_entry) > 0:  
        return [ prog_load_entry[0], re.findall(r"\[(\d{6})\]",  zeile)[0],  get_date_hour_min(zeile) ]
    else:
        return None            
       
       
# Liste wird mit Tupel befüllt, welsche die Meldungs-Paaren enthalten
def state_machine():
    status_server_start = "wait"
    status_prog_load = "wait"
    counter = 0
    with open('ausgabe.log', 'r') as eingabe:             
        for zeile in eingabe:
            if  status_server_start != "run":             
                server_start_line = get_server_start_line(zeile)   
                if  server_start_line  is not None:    #  and status_server_start != "run"
                    status_server_start = "run"
                    continue
            if  status_server_start == "run"  and status_prog_load == "wait": 
                if counter < 4:
                    counter = counter + 1
                    number_load_programs_line = get_number_load_programs_line(zeile)
                    if  number_load_programs_line is not None: 
                        # muss Liste von Strings von hier schicken
                        create_log_message_entry(server_start_line, number_load_programs_line)
                        status_server_start = "wait"
                        status_prog_load = "wait"
                        counter = 0
                        break
                else:
                    print("aaaaaaaaaaaaaaaa")
                    create_log_message_entry(server_start_line, "missing")
                    status_server_start = "wait"
                    status_prog_load = "wait"
                    counter = 0                           
                    break                                    
                # else:
                    # x = ''
                # create_log_message_entry(server_start_line, "missing")
                # status_server_start = "wait"
                # status_prog_load = "wait"
                # counter = 0       
 
def main():
    state_machine()

if __name__ == "__main__":
    main()


        
        
        
        
        
        

