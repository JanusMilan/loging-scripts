class FrontendErrors:
    """ includes all previously known types of  frontend errors"""
    known_frontend_errors =  {
            ".*ReferenceError:" :
                {
                    " OpenRoberta is not defined" : []     
                },        
            ".*fn3 caught an EXCEPTION:" :
                {
                    " TypeError: Cannot read property 'reset' of undefined" : [],
                    " TypeError: Unable to get property 'reset' of undefined or null reference" : [],
                    " TypeError: undefined is not an object \(evaluating 'robots\[i\].reset'\)" : [],                    
                    " TypeError: robots\[i\] is undefined" : [],
                    " TypeError: result is undefined" : [],
                    " Error: Syntax error, unrecognized expression: \#escape\[object Object\]" : [],
                    " TypeError: Cannot read property 'replaceState' of undefined" : []
                },
            ".*appToJsInterface" :
                {
                    " >TypeError: undefined is not an object .*" : [],
                    " >invalid arguments caused by: .*" : []            
                },
            ".*jsToAppInterface" :
                {
                    " >Error: Java exception was raised during method invocation caused by: \[object Object\]" : []
                },
            ".*saveToServer" :  
                {
                    " may only be called with an explicit config name" : []
                },
            ".*tabConfiguration clicked, then EXCEPTION:" :
                {                                                                
                    " TypeError: t is undefined" : [],
                    " TypeError: undefined has no properties" : [],
                    " TypeError: Cannot read property 'selector' of undefined" : [],
                    " TypeError: can't access property \"selector\", t is undefined" : [],
                    " TypeError: Unable to get property 'selector' of undefined or null reference" : [],
                    " TypeError: Die Eigenschaft \"selector\" eines undefinierten oder Nullverweises kann nicht abgerufen werden." : [],
                    " TypeError: undefined is not an object \(evaluating 't.selector'\)" : []
                 },    
            ".*robot choosen in start popup, then EXCEPTION:" :
                {
                    " TypeError: Cannot read property 'info' of undefined" : [],
                    " TypeError: GUISTATE_C.getRobots\(...\)\[choosenRobotType\] is undefined" : [],
                    " TypeError: undefined is not an object \(evaluating 'GUISTATE_C.getRobots\(\)\[choosenRobotType\].info'\)" : [],
                    " TypeError: Unable to get property 'info' of undefined or null reference" : [],
                    " TypeError: Cannot read property 'info' of undefined" : [],
                    " Error: Permission denied to access property \"apply\"" : [],
                    " TypeError: o\[i\].slick is undefined" : [],
                    " TypeError: Não é possível obter a propriedade 'info' de uma referência não definida ou nula" : []
                 },
            ".*set robot '(.)*', then EXCEPTION:" :
                {   
                    " TypeError: Cannot read property 'selector' of undefined" : [],
                    " TypeError: W.stepData is undefined" : [],
                    " TypeError: HELP_C.initView is not a function" : [],     
                    " TypeError: undefined is not an object \(evaluating 'W.stepData.enjoyHintElementSelector'\)" : [],         
                    " TypeError: t is undefined" : [],
                    " TypeError: Unable to get property '.*' of undefined or null reference" : [],                        
                    " TypeError: undefined has no properties" : [],              
                    " TypeError: result is undefined" : [],
                    " TypeError: Cannot read property 'enjoyHintElementSelector' of undefined" : [],
                    " TypeError: Cannot read property 'listRobotStop' of undefined" : []
                 },            
            ".*load gallery list, then EXCEPTION:" :
                {             
                    " TypeError: result is undefined" : [],
                    " out of memory" : []
                 },             
            ".*gallery clicked, then EXCEPTION:" :
                {     
                   " Error: Permission denied to access property \"apply\"" : []
                 },                      
            ".*got user info from server, then EXCEPTION:" :
                {            
                    " TypeError: successFn is not a function. \(In 'successFn\(response\)', 'successFn' is undefined\)" : [],
                    " TypeError: successFn is not a function" : [],
                    " TypeError: Object expected" : [],
                    " TypeError: Objekt erwartet" : []
                 },         
            ".*clear user, then EXCEPTION:" :
                {           
                    " TypeError: result is undefined" : [],
                    " TypeError: UTIL.response is not a function" : []
                 },         
            ".*show source code of program '.*', then EXCEPTION:" :
                {         
                    " Error: Unspecified error.": [],
                    " Error: Error no especificado": [],
                    " TypeError: Object expected": [],
                    " TypeError: Cannot read property 'css' of null": [],                 
                    " TypeError: t is undefined": [],
                    " TypeError: Cannot read property 'selector' of undefined": [],
                    " TypeError: successFn is not a function. \(In 'successFn\(response\)', 'successFn' is undefined\)": [], 
                    " TypeError: successFn is not a function": [], 
                    " TypeError: undefined has no properties": [],
                    " TypeError: Unable to get property 'selector' of undefined or null reference": [],  
                    " TypeError: Die Eigenschaft \"selector\" eines undefinierten oder Nullverweises kann nicht abgerufen werden.": [],        
                    " TypeError: Objekt erwartet": [],
                    " TypeError: Se esperaba un objeto": [],
                    " TypeError: Предполагается наличие объекта": [],
                    " Blockly.Xml.textToDom did not obtain a valid XML tree.": []
                 },   
            ".*run program '.*' with configuration '.*', then EXCEPTION:" : 
                {               
                    " TypeError: robots\[i\] is undefined": [],
                    " TypeError: Cannot read property 'replaceState' of undefined": [],      
                    " TypeError: undefined is not an object \(evaluating 'robots\[i\].replaceState'\)": [],
                    " TypeError: result is undefined": [],
                    " TypeError: Cannot read property 'css' of null": [],              
                    " Error: Mismatched anonymous define\(\) module: function mustacheFactory \(mustache\) {" : [],
                    " Error: Zugriff verweigert" : [],
                    " Error: Unspecified error." : [],
                    " Error: Error no especificado.": [],
                    " Blockly.Xml.textToDom did not obtain a valid XML tree.": [], 
                    " Connection checks failed." : [],
                    " SyntaxError: Unexpected token u in JSON at position 0" : [],
                    " SyntaxError: JSON Parse error: Unexpected identifier \"undefined\"" : [],
                    " TypeError: Unable to get property 'replaceState' of undefined or null reference" : [],
                    " TypeError: Не удалось получить свойство \"replaceState\" ссылки, значение которой не определено или является NULL": [],
                    " Error: Mismatched anonymous define\(\) module: function\(\){\"use strict\".*" : [],
                    " Error: Mismatched anonymous define\(\) module: function\(t\){\"use strict\".*" : [],
                    " Error: Permission denied to access property \"apply\"" : [],
                    " TypeError: null is not an object \(evaluating 'this.\$backdrop.css'\)" : [],
                    " TypeError: Cannot read property 'modes' of undefined" : []  
                 },   
            ".*simScene clicked, then EXCEPTION:" :
                {                       
                    " TypeError: Cannot read property 'debug' of undefined" : [],
                    " TypeError: undefined is not an object \(evaluating 'robots\[0\].debug'\)" : [],
                    " TypeError: robots\[0\] is undefined" : [],
                    " TypeError: Unable to get property 'debug' of undefined or null reference" : [],
                    " TypeError: Cannot read property 'image' of null"  : []
                 },             
            ".*import clicked, then EXCEPTION:" :
                {       
                    " TypeMismatchError"  : []
                 }, 
            ".*Client connection issue:" :
                {            
                    " 0"  : [],        
                    " 200"  : [],
                    " 401"  : [],   
                    " 413"  : [],
                    " 499"  : [],
                    " 500"  : [],
                    " 503"  : []
                 },     
            ".*program edit clicked, then EXCEPTION:" :
                {          
                    " Error: Permission denied to access property \"apply\""  : [],
                    " Error: Der Remoteprozeduraufruf ist fehlgeschlagen."  : []
                 },                 
            ".*simResetPose clicked, then EXCEPTION:" :
                {        
                    " TypeError: Cannot read property 'resetPose' of undefined"  : [],
                    " TypeError: robots\[i\] is undefined"  : []
                 },                 
            ".*sim clicked, then EXCEPTION:" :
                {    
                    " TypeError: Cannot read property 'debug' of undefined"  : []
                 },    
             ".*simScene clicked, then EXCEPTION:" :
                {    
                    " TypeError: Cannot read property 'debug' of undefined"  : []
                 },                
            ".*head navigation menu item clicked, then EXCEPTION:" :
                {  
                    " Error: Error no especificado."  : []
                 },
             "NEW ERROR TYPE: " :
                {  
                   
                 }            
        }