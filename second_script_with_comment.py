import re

# Funktion zur Generierung des Messages und für die Ausgabe in Datei 'output.log'
def create_log_message_entry(server_start_entry, prog_load_entry):      
    with open('output.log', 'a+') as output:     
        # Fall 1: Server hat Programme NICHT geladen  UND  startete planmässig
        if prog_load_entry != 'missing' and server_start_entry[1] == '03:00':
            output.write('INFO: server started at: ' + server_start_entry[0] + ';  INFO: loaded ' + prog_load_entry[1] + ' programs' + "\n")  
        # Fall 2: Server hat Programme NICHT geladen UND startete NICHT planmässig    
        elif prog_load_entry != 'missing' and server_start_entry[1]  != '03:00' :    
            output.write('ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + '; INFO: loaded ' + prog_load_entry[1] + ' programs' + "\n")  
        # Fall 3: Server hat Programme geladen UND startete planmässig  
        elif prog_load_entry == 'missing' and server_start_entry[1] == '03:00' :
            output.write('INFO: server started at: ' + server_start_entry[0] + ': ERROR programs are not loaded' + "\n")
        # Fall 4. Server hat Programme NICHT geladen UND startete NICHT planmässig  
        else:
            output.write('ERROR: server started UNSCHEDULED at: ' + server_start_entry[0] + ': ERROR programs are not loaded' + "\n")

# State Machine Funktion zum Suchen der Meldungen
def find_enties():
    status_server_start = "wait"
    counter = 0
    with open('ausgabe.log', 'r') as eingabe:             
        for zeile in eingabe:
            # Datum der aktuellen Meldung\Zeile 
            date = re.match(r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2})", zeile)
            if  status_server_start == "wait": 
                # Meldung "..server started at.." suchen 
                if  re.search(r"server started at http://0.0.0.0:1999" , zeile)  is not None: 
                    # Meldung "..server started at.." ist gefunden
                    status_server_start =  [ date[0],  date[1] ]
                    continue
            # Falls Meldung "..server started at.." gefunden wird: 
            if  status_server_start != "wait": 
                # Dann kann Meldung "..Number of programs stored.." gesucht werden
                if counter < 2:
                    counter = counter + 1
                    # Suchen Meldung "..Number of programs stored.."
                    if  len( re.findall(r"Number of programs stored in the database", zeile) ) > 0 : 
                        # Falls Meldung "..Number of programs stored.."  gefunden wird, 
                        # dann wird sie zusammen mit der Meldung "..server started at.." an die Funktion "create_log_message_entry()" zur Auswertung übergeben
                        create_log_message_entry(status_server_start, [ date[0] , re.findall(r"\[(\d{1,})\]", zeile)[0]] )
                        # Dann können Flag und Conter für den nächsten Lauf gesetzt werden
                        status_server_start = "wait"
                        counter = 0
                #  Falls KEINE Meldung "..Number of programs stored.."  zum Meldung "..server started at.." gefunden wird           
                else:
                    # Dann wird String "missing" zusammen mit der Meldung "..server started at.." an Funktion "create_log_message_entry()" zur Auswertung übergeben
                    create_log_message_entry(status_server_start, "missing")
                    status_server_start = "wait"
                    counter = 0                           
                    
def main():
    find_enties()

if __name__ == "__main__":
    main()


        
        
        
        
        
        

