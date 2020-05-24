
################ Programm search_daily_errors.py
############################################################################# 
Allgemeines zum Programm
-> Es wird beliebige monatliche Log Datei analysiert 
-> Log Datei beinhaltet die Meldungen für Server Start (standardmässig um 03:00)
-> Programm lädt alle ERROR LOG Zeile für ganze Tag, wobeit zu prüfende Tag interaktiv eingegeben wird
-> Skizze des Programms:
  -> Program wird gestartet mit Angabe des prüfenden Monats und Tags  	
  -> Programm lädt  Log File für zu prüfendes Monat
  -> Im Log File wird nach Meldung für Server Start am vorgegebenem Datum gesucht
  -> Alle Meldungen LOG ERROR für diesen Tag bis zum nächsten Sarver Start rausgesucht und in eine Datei ausgegeben 
