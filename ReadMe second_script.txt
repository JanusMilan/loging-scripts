

Use Case
--> Flags werden für Regelung der State Machine eingesetzt
--> State Machine startet die .log Datei zeilenweise auf Meldung '..server started..' zu durchsuchen
    --> Meldung '..server started..'  wird mit Hilfe der Funktion 'get_server_start_line'  ausgewertet
	--> Wenn Meldung '..server started..' gefunden ist
		 --> Dann werden nächste vier Zeilen des Dokuments nach dem nach Meldung '..number of load programs..'   durchsucht
		      --> Meldung '..server started..'  wird mit Hilfe der Funktion 'get_number_load_programs_line'  ausgewertet
		      --> Falls  Meldung  '..number of load programs..'   gefunden wird
			       --> Dann werden beide Meldungen zur Auswertung an Funktion 'create_log_message_entry' übergeben
			            --> Hier sind  Fällen möglich
						     --> Meldung '..server started..'  hat kein entsprechenes Gegen-Meldung '..number of load programs..'  
							 --> Meldung '..server started..'  hat entsprechenes Gegen-Meldung '..number of load programs..'  UND Start hat planmässig stattgefunden
							 --> Meldung '..server started..'  hat entsprechenes Gegen-Meldung '..number of load programs..'  UND Start hat NICHT planmässig stattgefunden							 
		      --> Falls  Meldung  '..number of load programs..'  NICHT gefunden wird	
			       --> Dann werden beide Meldungen zur Auswertung an Funktion 'create_log_message_entry' übergeben
                      				   
