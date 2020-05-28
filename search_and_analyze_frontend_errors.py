import re
import sys 
from enum import Enum

    """ includes all previously known types of  frontend errors"""
frontend_errors =  {
        ".*ReferenceError:" :
            {
                " OpenRoberta is not defined" : " ("      
            },        
        ".*fn3 caught an EXCEPTION:" :
            {
                " TypeError: Cannot read property 'reset' of undefined" : " (",
                " TypeError: Unable to get property 'reset' of undefined or null reference" : " (",
                " TypeError: undefined is not an object \(evaluating 'robots\[i\].reset'\)" : " (",
                " TypeError: robots\[i\] is undefined" : " (",
                " TypeError: result is undefined" : "(",
                " Error: Syntax error, unrecognized expression: \#escape\[object Object\]" : " (",
                " TypeError: Cannot read property 'replaceState' of undefined" : " ("
            },
        ".*appToJsInterface" :
            {
                " >TypeError: undefined is not an object .*" : " (",
                " >invalid arguments caused by: .*" : " ("             
            },
        ".*jsToAppInterface" :
            {
                # " >invalid webview type caused by: \[object Object\]" : " (",           # rausgenommen von Reinhard
                " >Error: Java exception was raised during method invocation caused by: \[object Object\]" : " ("
            },
        ".*saveToServer" :  
            {
                " may only be called with an explicit config name" : " (" # 
            },
        ".*tabConfiguration clicked, then EXCEPTION:" :
            {                                                                
                " TypeError: t is undefined" : " (",
                " TypeError: undefined has no properties" : " (",
                " TypeError: Cannot read property 'selector' of undefined" : " (",
                " TypeError: can't access property \"selector\", t is undefined" : " (",
                " TypeError: Unable to get property 'selector' of undefined or null reference" : " (",
                " TypeError: Die Eigenschaft \"selector\" eines undefinierten oder Nullverweises kann nicht abgerufen werden." : " (",
                " TypeError: undefined is not an object \(evaluating 't.selector'\)" : " ("
             },    
        ".*robot choosen in start popup, then EXCEPTION:" :
            {
                " TypeError: Cannot read property 'info' of undefined" : " (",
                " TypeError: GUISTATE_C.getRobots\(...\)\[choosenRobotType\] is undefined" : " (",
                " TypeError: undefined is not an object \(evaluating 'GUISTATE_C.getRobots\(\)\[choosenRobotType\].info'\)" : " (",
                " TypeError: Unable to get property 'info' of undefined or null reference" : " (",
                " TypeError: Cannot read property 'info' of undefined" : " (",
                " Error: Permission denied to access property \"apply\"" : " (",
                " TypeError: o\[i\].slick is undefined" : "(",
                " TypeError: Não é possível obter a propriedade 'info' de uma referência não definida ou nula" : " ("
             },
        ".*set robot '(.)*', then EXCEPTION:" :
            {   
                " TypeError: Cannot read property 'selector' of undefined" : " (",
                " TypeError: W.stepData is undefined" : " (",
                " TypeError: HELP_C.initView is not a function" : " (",     
                " TypeError: undefined is not an object \(evaluating 'W.stepData.enjoyHintElementSelector'\)" : " (",         
                " TypeError: t is undefined" : "(",
                " TypeError: Unable to get property '.*' of undefined or null reference" : " (",                        
                " TypeError: undefined has no properties" : " (",              
                " TypeError: result is undefined" : " (",
                " TypeError: Cannot read property 'enjoyHintElementSelector' of undefined" : " (",
                " TypeError: Cannot read property 'listRobotStop' of undefined" : " ("
             },            
        ".*load gallery list, then EXCEPTION:" :
            {             
                " TypeError: result is undefined" : " (",
                " out of memory" : "("
             },             
        ".*gallery clicked, then EXCEPTION:" :
            {     
               " Error: Permission denied to access property \"apply\"" : " (" 
             },                      
        ".*got user info from server, then EXCEPTION:" :
            {            
                " TypeError: successFn is not a function. \(In 'successFn\(response\)', 'successFn' is undefined\)" : " (",
                " TypeError: successFn is not a function" : " (",
                " TypeError: Object expected" : " (",
                " TypeError: Objekt erwartet" : " ("
             },         
        ".*clear user, then EXCEPTION:" :
            {           
                " TypeError: result is undefined" : " (",
                " TypeError: UTIL.response is not a function" : " ("
             },         
        ".*show source code of program '.*', then EXCEPTION:" :
            {         
                " Error: Unspecified error.": " (",
                " Error: Error no especificado": " (",
                " TypeError: Object expected": " (",
                " TypeError: Cannot read property 'css' of null": " (",                 
                " TypeError: t is undefined": " (",
                " TypeError: Cannot read property 'selector' of undefined": " (",
                " TypeError: successFn is not a function. \(In 'successFn\(response\)', 'successFn' is undefined\)": " (", 
                " TypeError: successFn is not a function": " (", 
                " TypeError: undefined has no properties": " (",
                " TypeError: Unable to get property 'selector' of undefined or null reference": " (",  
                " TypeError: Die Eigenschaft \"selector\" eines undefinierten oder Nullverweises kann nicht abgerufen werden.": " (",        
                " TypeError: Objekt erwartet": " (",
                " TypeError: Se esperaba un objeto": " (",
                " TypeError: Предполагается наличие объекта": " (",
                " Blockly.Xml.textToDom did not obtain a valid XML tree.": " (" 
             },   
        ".*run program '.*' with configuration '.*', then EXCEPTION:" : #
            {               
                " TypeError: robots\[i\] is undefined": " (",
                " TypeError: Cannot read property 'replaceState' of undefined": " (",      
                " TypeError: undefined is not an object \(evaluating 'robots\[i\].replaceState'\)": " (",
                " TypeError: result is undefined": " (",
                " TypeError: Cannot read property 'css' of null": " (",              
                " Error: Mismatched anonymous define\(\) module: function mustacheFactory \(mustache\) {" : " (",
                " Error: Zugriff verweigert" : " (",
                " Error: Unspecified error." : " (",
                " Error: Error no especificado.": " (",
                " Blockly.Xml.textToDom did not obtain a valid XML tree.": " (", 
                " Connection checks failed." : " (",
                " SyntaxError: Unexpected token u in JSON at position 0" : " (",
                " SyntaxError: JSON Parse error: Unexpected identifier \"undefined\"" : " (",
                " TypeError: Unable to get property 'replaceState' of undefined or null reference" : " (",
                " TypeError: Не удалось получить свойство \"replaceState\" ссылки, значение которой не определено или является NULL": " (",
                " Error: Mismatched anonymous define\(\) module: function\(\){\"use strict\".*" : " (",
                " Error: Mismatched anonymous define\(\) module: function\(t\){\"use strict\".*" : " (",
                " Error: Permission denied to access property \"apply\"" : " (",
                " TypeError: null is not an object \(evaluating 'this.\$backdrop.css'\)" : " (",
                " TypeError: Cannot read property 'modes' of undefined" : " ("   
             },   
        ".*simScene clicked, then EXCEPTION:" :
            {                       
                " TypeError: Cannot read property 'debug' of undefined" : " (",
                " TypeError: undefined is not an object \(evaluating 'robots\[0\].debug'\)" : " (",
                " TypeError: robots\[0\] is undefined" : " (",
                " TypeError: Unable to get property 'debug' of undefined or null reference" : " (",
                " TypeError: Cannot read property 'image' of null"  : " ("
             },             
        ".*import clicked, then EXCEPTION:" :
            {       
                " TypeMismatchError"  : " ("
             }, 
        ".*Client connection issue:" :
            {            
                " 0"  : " (",        
                " 200"  : " (",
                " 401"  : " (",   
                " 413"  : " (",
                " 499"  : " (",
                " 500"  : " (",
                " 503"  : " ("
             },     
        ".*program edit clicked, then EXCEPTION:" :
            {          
                " Error: Permission denied to access property \"apply\""  : " (",
                " Error: Der Remoteprozeduraufruf ist fehlgeschlagen."  : " ("
             },                 
        ".*simResetPose clicked, then EXCEPTION:" :
            {        
                " TypeError: Cannot read property 'resetPose' of undefined"  : " (",
                " TypeError: robots\[i\] is undefined"  : " ("
             },                 
        ".*sim clicked, then EXCEPTION:" :
            {    
                " TypeError: Cannot read property 'debug' of undefined"  : " ("
             },    
         ".*simScene clicked, then EXCEPTION:" :
            {    
                " TypeError: Cannot read property 'debug' of undefined"  : " ("
             },                
        ".*head navigation menu item clicked, then EXCEPTION:" :
            {  
                " Error: Error no especificado."  : " ("
             }
    }
    
    
def search_client_logger_errors(infile):
    """ for searching for all monthly frontend errors 
    :param: infile: .log file with data to  evaluate 
    """
    with open(infile, 'r') as file: 
        for line_number,line in enumerate(file):
            client_logger_error = re.search(r" d.fhg.iais.roberta.util.ClientLogger - log entry: \[\[ERR \]\] (.*)", line)
            if client_logger_error is not None:
                analyze_error(line, str(line_number))                
                continue
            else:
                continue    
    
    
class MachineState(Enum):
    """ Enum-Class serves for implementation of state machine status """
    search_error = 1
    found_error = 2   
    

def analyze_error(line, line_number_of_error):  
    """ for analyzing the monthly errors: Assign errors to error group and error type
        :param: line: line with error
        :param: line_number_of_error: line number of the error        
    """     
    machine_state = MachineState.search_error
    for error_group,group_value  in frontend_errors.items(): 
        if machine_state == MachineState.search_error:
            for error_type in group_value:             
                if re.match(error_group + error_type, line) is not None:
                    frontend_errors[error_group][error_type] =  frontend_errors[error_group][error_type] + line_number_of_error + ","
                    machine_state = MachineState.found_error
                    break
                else:                         
                    continue
        elif machine_state == MachineState.found_error:
            return
        else:
            raise Exception('machine_state is invalid. The value of machine_state was: {}'.format(machine_state))     
    if machine_state == MachineState.search_error:
        message = re.split('msec: ',line)
        if len(message) == 2:                
            error_type = re.match("(.*EXCEPTION:)(.*)", message[1])
        else:
            error_type = re.match(".*(\[\[ERR \]\])(.*)", line) 
        frontend_errors.update({'NEW ERROR TYPE: ' + error_type[1]:{error_type[2]: '(' +line_number_of_error + ","}} )  
        return 
    elif machine_state == MachineState.found_error:
        return
    else:
        raise Exception('Sstate machine is invalid. The value of machine_state was: {}'.format(machine_state))          

                
def write_output_file(outfile):    
    """ for formating of output and for output into outputfile
        :param: outfile: output file for the evalation data
    """                 
    with open(outfile, 'w+') as f: 
        for error_group,value  in frontend_errors.items():
            for error, error_enumeration in value.items():
                if frontend_errors[error_group][error].endswith(','):
                    frontend_errors[error_group][error] = frontend_errors[error_group][error][:-1]      
                    frontend_errors[error_group][error] = frontend_errors[error_group][error] + ")"                    
                    f.write(error_group +  error  + frontend_errors[error_group][error] + '\n') 
                else:
                    return
                
                
def main():
    """ main function serves for process control 
    how to run program: python3 search_and_analyze_frontend_errors.py test_infile_frontende_error.txt test_outfile_frontende_error.txt    
    """
    infile = ""    
    outfile = ""
    try:
        infile = sys.argv[1]
    except IndexError:
        sys.exit( "input file parameter missing")
    try:
        outfile = sys.argv[2]
    except IndexError:
        sys.exit("output file parameter missing")
    search_client_logger_errors(infile)
    write_output_file(outfile)    
    

if __name__ == "__main__":
    main()        