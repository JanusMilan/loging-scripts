
Was ist die Aufgabe des Programm
-> Es gibt monatliche Log Datei 
-> Log Datei beinhaltet unter anderen auch die Meldungen für Server Start
-> Maximal 4 Zeilen später kommt die zugehörige Meldung dass die User Programme geladen sind
-> Aufgabe des Programms ist:
  -> Programm lädt Log File und wertet es aus
  -> Es wird nach Meldung für Server Start gesucht
  -> Dann wird zugehörige Meldung "..Number of programs stored.." gesucht
  -> Beide Meldungen werden in Funktion "create_log_message_entry" ausgewertet
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
         -> Dann wird Ausgabe File in Funktion auswerten_server_start ausgewertet, 
		     --> ob alle Sertver Start regulär sind oder gibt es ERRORS
         -> Entsprechende Meldung wird im Ausgabe File am EOF angehängt	 

	
	 
	 

