import re

def write_error_files(entries_collection, file_name):
    """ write evaluation files
    :param: entries_collection: collection to be write in the file
    :param: file_name: name to be assigned to new file    
    """
    if file_name ==  "output_double_error_rows.log":
        with open('output_double_error_rows.log', 'w') as output_file:
            for element in entries_collection:
                output_file.write(element)
    if file_name == "output_error_rows.log":
        with open('output_error_rows.log', 'w') as output_file:
            for element in entries_collection.values():
                output_file.write(element)
    if file_name == "output_error_types.log":
        with open('output_error_types.log', 'w') as output_file:
            for element in entries_collection.values():
                output_file.write(element)                   

def search_error_entries(file_to_check: str, day_to_check: str):
    """ search for error entries in desired file
    use function write_error_files to generate file "output_error_rows.log" with all errors
    use function write_error_files to generate file "output_double_error_rows.log" with double errors
    :important: the two variables 'ignore_one' and 'ignore_two' make up 50% of the error entries
    :param: file_to_check: month log file to be check for errors
    :param: day_to_check: day to be check for errors
    """
    ignore_one = "Android Webview: ReferenceError: OpenRoberta is not defined"
    ignore_two = "no IOS Webview: TypeError: Cannot read property 'messageHandlers' of undefined"     
    status_server_start : str = "wait for server start"
    dict_of_entries = dict()
    list_of_double_entries = list()
    with open(file_to_check, 'r') as input_file:            
        for element in input_file:
            date_of_entry = re.search(r"\d{4}-(\d{2}-\d{2}) \d{2}:\d{2}", element)
            if  status_server_start == "wait for server start":
                if  re.search(r"server started at http://0.0.0.0:1999" , element)  is not None and date_of_entry[1] ==  day_to_check:
                    status_server_start = "found server start"
                    dict_of_entries.update({element: element})
                    continue
            if  status_server_start == "found server start":
                if re.search(r"server started at http://0.0.0.0:1999" , element)  is not None:
                    dict_of_entries.update({element: element})
                    break
                if re.search(ignore_one,  element) is None and re.search(ignore_two,  element) is None and re.search(r"ERR",  element,  re.IGNORECASE) is not None:      
                    if element in dict_of_entries:
                        list_of_double_entries.append(dict_of_entries[element])
                    dict_of_entries.update({element: element})
    write_error_files(dict_of_entries, "output_error_rows.log" )
    write_error_files(list_of_double_entries, "output_double_error_rows.log" )

def search_error_types():
    """ filters file by error type, in dictionary occurs each type only once
    use function write_error_files to generate file "output_error_types.log" with types of error
    """
    dict_of_error_types = dict()    
    with open('output_error_rows.log', 'r') as input_file:      
        for element in input_file:
            if re.search(r"robot-name=\[\w{0,}\d{0,}\w{0,}\]", element) is not None:
                only_error_type = re.split(r"robot-name=\[\w{0,}\d{0,}\w{0,}\] ", element)
                dict_of_error_types.update({only_error_type[1]: only_error_type[1]})
            # for unusual errors like '/opt/ora-cc-rsc/...'    
            else:
                dict_of_error_types.update({element: element})
    write_error_files(dict_of_error_types, 'output_error_types.log')

def main():
    """ main function """  
    month_to_check = input("please enter month (format example 04): ")
    day_to_check = month_to_check + "-" + input("please enter day (format example 01): ")        
    search_error_entries(month_to_check + ".log", day_to_check)
    search_error_types()
if __name__ == "__main__":
    main()