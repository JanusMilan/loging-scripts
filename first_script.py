import re
import io
import collections

#text = "A fat cat doesn't eat oat but a rat eats bats."
#regex = "[force]at"
#mo = re.findall(regex, text)
#print mo

# text = "333-333-666 444-333-666 5555-333-666 333.333.666 333.-333-.666"
# regex = "\d\d\d.\d\d\d.\d\d\d"                   # alle Ziffern durch 'd'            # alle Zeichen durch Metazeichen '.'  
# regex1 = "\d\d\d[\.-]\d\d\d[\.-]\d\d\d"         # Demaskieren '.' durch '\'     # '[]' Gruppierung mit ENTWEDER ODER durch '[]'    
# mo = re.findall(regex1, text)
# print (mo)


# regex = re.compile(r"ERROR")             # 'r' sagt dem Phytone dass er String "ERROR" nicht als gewöhliche sondern als Regex String behandeln soll
# print(type(regex))                               # 'regex' ist ein Pattern Objekt

# with open('04.log', 'r') as datei:             # datei ist Objekt, also kein String oder Liste
    # for zeile in datei:        
        # #  print(type(zeile))                       # 'zeile' ist ein String
        # m = regex.findall(zeile)                 # 'findall' prüft 'zeile' auf 'regex', 'regex' wird in Liste 'm' genomen so oft wie er in der 'zeile' vorkommt (0 bis x mal)
        # #  print(type(m))                           # 'm' ist eine Liste       
        # if len(m) > 0:                               # Falls Liste 'm' Elemente enthält dann enthält die 'zeile' den 'regex' 
            # print(zeile.strip())                    # Zeile nat immer am Ende \n (NewLine) also stripen
# datei.close()

# Befüllen "ausgabe.txt'" um dies für Proggen und Testen zu nutzen
# serverStartedRegex = re.compile(r"server started at http://0.0.0.0:1999") 
# numberOfProgramsRegex = re.compile(r"Number of programs stored in the database")   
# output = dict()                                             #dictionary    
# with open('04.log', 'r') as eingabe:             
    # for index, zeile in enumerate(eingabe):        
        # serverStartedZeile = serverStartedRegex.findall(zeile) 
        # numberOfProgramsZeile = numberOfProgramsRegex.findall(zeile)        
        # if len(serverStartedZeile) > 0  or len(numberOfProgramsZeile) >  0 :    
            # output.update({str(index) : zeile})        
            # with open('ausgabe.txt', 'a') as ausgabe:
                # ausgabe.write(str(index) + ":" + zeile)
# for key in output:
    # print(key)       
# for value in output.values():    
    #print(value)       
    
# Befüllen zwei Dictionaries 
# Dictionary server_start_entries_dict enthält Meldungen "server started at http://0.0.0.0:1999" 
# Dictionary number_prog_entry_entries_dict enthält Meldungen "Number of programs stored in the database" 
server_start_date_key_entry_regex =  re.compile(r"2020-\d{2}-\d{2} \d{2}:\d{2}") 
server_start_entries_dict = dict()       
server_start_entries_regex =  re.compile(r"server started at http://0.0.0.0:1999") 
number_prog_entry_entries_dict = dict()         
number_prog_entry_entries_regex =  re.compile(r"Number of programs stored in the database: \[\d{6}\]")   
with open('ausgabe.txt', 'r') as eingabe:             
    for zeile in eingabe:        
        server_start_date_key_entry = server_start_entries_regex.search(zeile) 
        number_prog_entry = number_prog_entry_entries_regex.search(zeile) 
        start_date_key = server_start_date_key_entry_regex.search(zeile)        
        if server_start_date_key_entry is not None:
            server_start_entries_dict.update({start_date_key.group(): server_start_date_key_entry.group()})
        if number_prog_entry is not None:
            number_prog_entry_entries_dict.update({start_date_key.group() : number_prog_entry.group()})
# for key in server_start_entries_dict:
    # print(key)     
# for value in server_start_entries_dict.values():    
    # print(value)       
# for key in number_prog_entry_entries_dict:
    # print(key)     
# for value in number_prog_entry_entries_dict.values():    
    # print(value)       

# vergleichen zwei Dictionaries ob ihre einträge die Paare bilden
output_dict = dict()
number_prog_entry_regex =  re.compile(r"(\d{6})")                                                                                           # Anzahl der Programme 
# if prüfen welsche im  server_start_entries_dict sind und nicht im number_prog_entry_entries_dict
# if len(server_start_entries_dict) > len(number_prog_entry_entries_dict)
for key in number_prog_entry_entries_dict:
    if  key in server_start_entries_dict:
        number_prog_entry = number_prog_entry_regex.search(number_prog_entry_entries_dict.get(key))                     
        output_dict.update({key: "server started on:" + key + ", Number of programs stored in the database:" +number_prog_entry.group()}) 
    if  server_start_entries_dict.get(key) == None:        
        output_dict.update({key: "ERROR: on " + key + " is \'server started at http://0.0.0.0:1999\' entry missing"})
# prüfen welsche im number_prog_entry_entries_dict sind und nicht im server_start_entries_dict
# if len(number_prog_entry_entries_dict) > len(server_start_entries_dict)
for key in server_start_entries_dict :
    if  key in number_prog_entry_entries_dict:
        number_prog_entry = number_prog_entry_regex.search(number_prog_entry_entries_dict.get(key))
        output_dict.update({key: "server started on " + key + ", Number of programs stored in the database " +number_prog_entry.group()})
    if  not key in number_prog_entry_entries_dict:
        output_dict.update({key: "ERROR: on " + key + " is \'Number of programs stored in the database\' entry missing"})       

#OrderedDict (geordnete Dictionary)
sort_output_dict = collections.OrderedDict(sorted(output_dict.items()))

# Prüfen ob es unplanmäßige Reboot war
start_hour_regex =  re.compile(r"2020-\d{2}-\d{2} (\d{2}:\d{2})")                                                                           #  '()' group bilden um Uhrzeit zu fangen
for key in sort_output_dict :
    start_hour = start_hour_regex.match(key)
    if start_hour.group(1)  != "03:00":   
        tmp_string =  "ERROR: start of server at " + start_hour.group(1) + " o'clock,  " + sort_output_dict.get(key) 
        sort_output_dict.update({key: tmp_string}) 

with open('output.txt', 'w') as output:
    for value in sort_output_dict.values():    
        output.write(value + "\n")

 # ToDo 
 # wie oft wird Script ausgefüht 
 # automatisch im cron UND immer letzt xyz.log automatisch laden? aktuelle Monat? letzte volle Monat? 
 # manuell auführen und mit input Monat zu prüfen wählen?


 
 
 
            
            
        
            


