Allgemeines zum Programm
-> Es gibt monatliche Log Datei 
-> Log Datei beinhaltet unter anderen auch die Meldungen für Server Start
-> Maximal 4 Zeilen später kommt die zugehörige Meldung dass die User Programme geladen sind
-> Programm überprüft ob Server Start regulär und regelmässig sind
-> Skizze des Programms:
  -> Programm lädt Log File und wertet es aus
  -> Es wird nach Meldung für Server Start gesucht
  -> Dann wird zugehörige Meldung "..Number of programs stored.." gesucht
  -> Beide Meldungen werden in Funktion "evaluate_server_start_entry" ausgewertet
     -> Prüfenn ob der Server planmäßig um 03:00 gestartet wurde
	 -> Prüfenn ob nach server Start die User Programme geladen sind
     -> Nach Auswertung des Programms wird das Ergebnis in einer Ausgabe File ausgegeben
         -> Mögliche Ergebnisse (je nach Fall) sind: 	 
			 --> Server startete planmässig und Programme sind geladen 
			 --> Server startete NICHT planmässig und Programme sind geladen 
			 --> Server startete planmässig und Programme sind NICHT geladen 			
			 --> Server startete NICHT planmässig und Programme sind NICHT geladen 	
  -> Es wird sukzessive nach weiteren Meldungen für Server Start gesucht bim zum EOF
  -> Wenn alle Meldungen für Server Start im Log Datei erfasst sind
         -> Dann wird Ausgabe File in Funktion "evaluate_server_starts" ausgewertet, 
		     --> ob alle Sertver Start regulär sind oder gibt es ERRORS
         -> Entsprechende Meldung wird im Ausgabe File am EOF angehängt	
		 
To test programm from folder with program "search_server_error.py" 
--> go to folder: "cd test_files/search_server_error/"
--> Start the programm in the console: "python3 ../../search_server_error.py  test_input.txt  test_output.txt"

OR put test files together with program file in the same folder
--> Start the programm in the console: "python3 search_server_error.py  test_input.txt  test_output.txt"
