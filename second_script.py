import re
import sys

# Funktion zur Generierung des Messages und für die Ausgabe in Datei 'output.log'
def create_log_message_entry(server_start_entry: list, prog_load_entry: str ) -> str:      
    with open('output.txt', 'a+') as output:     
        if prog_load_entry != 'missing' and server_start_entry[1] == '03:00':
            output.write('INFO: server started at: ' + server_start_entry[0] + ';  INFO: loaded ' + prog_load_entry[1] + ' programs' + "\n")  
        elif prog_load_entry != 'missing' and server_start_entry[1]  != '03:00' :    
            output.write('ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + '; INFO: loaded ' + prog_load_entry[1] + ' programs' + "\n")  
        elif prog_load_entry == 'missing' and server_start_entry[1] == '03:00' :
            output.write('INFO: server started at: ' + server_start_entry[0] + ': ERROR programs are not loaded' + "\n")
        else:
            output.write('ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + ': ERROR programs are not loaded' + "\n")

# State Machine Funktion zur Suchen der Meldungen
def find_enties():
    """ Sucht die Log Datei nach Meldungen "..server started at.." und "..Number of programs stored.."   
    gibt beide Meldungen an die "create_log_message_entry" Funktion weiter zur Auswertung
    arguments:
    param: status_server_start: flag für Steurung der State Machine  
    :returns: gibt nicht zurück
    """
    status_server_start = "wait"
    counter = 0
    with open('ausgabe.log', 'r') as eingabe:             
        for zeile in eingabe:
            date = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", zeile)
            if  status_server_start == "wait": 
                if  re.search(r"server started at http://0.0.0.0:1999" , zeile)  is not None: 
                    status_server_start =  [ date[0],  date[1] ]
                    continue
            if  status_server_start != "wait": 
                if counter < 2:
                    counter = counter + 1
                    if  len( re.findall(r"Number of programs stored in the database", zeile) ) > 0 : 
                        create_log_message_entry(status_server_start, [ date[0] , re.findall(r"\[(\d{1,})\]", zeile)[0]] )
                        status_server_start = "wait"
                        counter = 0
                else:
                    create_log_message_entry(status_server_start, "missing")
                    status_server_start = "wait"
                    counter = 0                             
                    
def main():
    # help(find_enties)
    #print(dir(find_enties))
    print(find_enties.__doc__)
    print(create_log_message_entry.__annotations__)
    #print(help(find_enties))
    find_enties()

if __name__ == "__main__":
    main()      
        
        
        
        

