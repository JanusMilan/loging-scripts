

Was ist die Aufgabe des Scripts
--> Wurde der Server gestartet und wurden die User-Programme geladen: Bilden beide Meldungen ein Paar?     
--> Wurde der Server planmäßig um 03:00 gestartet?

Ablauf
--> Funktion "main" ist Startpunkt des Skripts und sie ruft die State Machine Funktion "find_enties" aus
--> State Machine Funktion "find_entities" 
     --> Funktion öffnet die aktuelle Logdatei 
     --> Funktion	startet eine zeilenweise Suche nach der Meldung "..server started at.."
     --> Machine State hat Status "wait" bis diese Meldung gefunden wird
     --> Wenn diese Meldung gefunden wird, wechselt die State Machine in den aktiven Status 
	      --> Jetzt startet die Funktion eine zeilenweise Suche nach der Meldung "..Number of programs stored.." 
	      --> FALLS  Meldung  '..number of load programs..'   gefunden wird ODER FALLS  Meldung  '..number of load programs..'  NICHT gefunden wird:
			  --> Die relevanten Daten beider Meldungen werden zur Auswertung an Funktion 'create_log_message_entry' übergeben 
			  --> Der Unterschied zwischen zwei Fällen liegt im Inhalt der relevanten Daten für Meldung "..Number of programs stored.."
                      				   
Use Case Fall 
--> Cron-Daemon führt das Skript zur Auswertung der Log File aus
--> Skript lädt Log File und wertet es aus
--> Nach Auswertung des Skripts wird das Ergebnis in einer Ausgabe Log File ausgegeben 
--> In der Ausgabe Log File sind folgende Fälle möglich:
	 --> Server startete planmässig und Programme sind geladen 
	 --> Server startete NICHT planmässig und Programme sind geladen 
	 --> Server startete planmässig und Programme sind NICHT geladen 			
	 --> Server startete NICHT planmässig und Programme sind NICHT geladen 		
	 
	 

