import re                       # regex Modul     
import io                       # für Steams z.B. open()    
import collections          # für Collections, hier OrderedDict Dictionary
    
# Befüllen zwei Dictionaries 
# Dictionary server_start_entries_dict enthält Meldungen "server started at http://0.0.0.0:1999" 
# Dictionary number_prog_entry_entries_dict enthält Meldungen "Number of programs stored in the database" 
server_start_date_key_entry_regex =  re.compile(r"2020-\d{2}-\d{2} \d{2}:\d{2}") 
server_start_entries_dict = dict()       
server_start_entries_regex =  re.compile(r"server started at http://0.0.0.0:1999") 
number_prog_entry_entries_dict = dict()         
number_prog_entry_entries_regex =  re.compile(r"Number of programs stored in the database: \[\d{6}\]")   
with open('ausgabe.log', 'r') as eingabe:             
    for zeile in eingabe:        
        server_start_date_key_entry = server_start_entries_regex.search(zeile) 
        number_prog_entry = number_prog_entry_entries_regex.search(zeile) 
        start_date_key = server_start_date_key_entry_regex.search(zeile)        
        if server_start_date_key_entry is not None:
            server_start_entries_dict.update({start_date_key.group(): server_start_date_key_entry.group()})
        if number_prog_entry is not None:
            number_prog_entry_entries_dict.update({start_date_key.group() : number_prog_entry.group()})

# vergleichen zwei Dictionaries ob ihre einträge die Paare bilden
output_dict = dict()
number_prog_entry_regex =  re.compile(r"(\d{6})")                                                                                           
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
start_hour_regex =  re.compile(r"2020-\d{2}-\d{2} (\d{2}:\d{2})")                                                                           
for key in sort_output_dict :
    start_hour = start_hour_regex.match(key)
    if start_hour.group(1)  != "03:00":   
        tmp_string =  "ERROR: start of server at " + start_hour.group(1) + " o'clock,  " + sort_output_dict.get(key) 
        sort_output_dict.update({key: tmp_string}) 

with open('output.log', 'w') as output:
    for value in sort_output_dict.values():    
        output.write(value + "\n")

 
 
 
            
            
        
            


