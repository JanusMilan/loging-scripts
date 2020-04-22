Zu prüfen
--> Wurde Server gestartet und wurden die User-Programme geladen: Bilden beide Meldungen ein Paar?     
--> Wurde Server planmäßig um 03:00 gestartet?

Schritt 1
--> Zwei Dictionaries Instanziieren, die sollen dienen für Verpaarung der zugehörigen Meldungen
--> Meldungen 'server started at http://0.0.0.0:1999' in eigene Dictionary speichern
--> Meldungen 'Number of programs stored in the database' in eigene Dictionary speichern

Schritt 2
--> Prüfen ob Meldungen aus zwei Dictionaries die Paaren bilden
--> Zwei for Schleifen: je nach dem welche der zwei Dictionaries größer ist:
     --> ToDo: Koderedundanz: eine Funktion programmieren?
--> Falls es Meldungen gibt welsche kein Paar haben, wird entsprechene ERROR Meldung gemacht
--> Ergebnis ist dritte Dictionary 'output_dict' mit zugehörigen Medlungen
--> Dictionary 'output_dict' ist wegen if-s, bezüglich des Datum, unsortiert 

Schritt 3
--> Vierte sortierte Dictionary 'sort_output_dict' erstellen
--> Prüfen ob Serverstart planmäßig um 03:00 stattgefunden hat 
--> Falls es Meldungen mit einem nicht planmäßigem Serverstart gibt, wird entsprechene ERROR Meldung gemacht

Schritt 4
--> sortierte Dictionary 'sort_output_dict' in die Datei 'output.txt' rausschreiben






