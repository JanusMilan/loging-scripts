class BackendErrors:
    """ includes all previously known types of  backend errors"""
    
    known_backend_errors =  {
            ".*(INFO d.f.i.r.p.AbstractProcessor -)" : 
                {   
                    " Processor failed: USER_GET_ONE_ERROR_ID_OR_PASSWORD_WRONG" : [],              
                    " Processor failed: PROGRAM_GET_ONE_ERROR_NOT_FOUND" : [],                       
                    " Processor failed: PROGRAM_SAVE_AS_ERROR_PROGRAM_EXISTS" : [],
                    " Processor failed: USER_EMAIL_ONE_ERROR_USER_NOT_EXISTS_WITH_THIS_EMAIL" : [],                                      
                    " Processor failed: USER_CREATE_ERROR_NOT_SAVED_TO_DB" : [],                      
                    " Processor failed: USER_ERROR_EMAIL_USED" : [],                  
                    " Processor failed: PROGRAM_ERROR_ID_INVALID" : [],               
                    " Processor failed: PROGRAM_SAVE_ERROR_NO_WRITE_PERMISSION" : [],
                    " Processor failed: PROGRAM_GET_ONE_ERROR_NOT_LOGGED_IN" : [],    
                    " Processor failed: CONFIGURATION_ERROR_ID_INVALID" : [], 
                    " Processor failed: PROGRAM_SAVE_ERROR_OPTIMISTIC_TIMESTAMP_LOCKING" : [],
                    " Processor failed: LIKE_SAVE_ERROR_EXISTS" : [],
                    " Processor failed: USER_DELETE_ERROR_ID_NOT_FOUND" : [],
                    " Processor failed: PROGRAM_DELETE_ERROR" : [],
                    " Processor failed: USER_UPDATE_ERROR_ACCOUNT_WRONG" : [],
                    " Processor failed: USER_TO_SHARE_DOES_NOT_EXIST" : [],                   
                    " Processor failed: PROGRAM_SAVE_ERROR_PROGRAM_TO_UPDATE_NOT_FOUND" : [],
                    " Processor failed: CONFIGURATION_SAVE_ERROR" : [],
                    " Processor failed: USER_ERROR_NOT_LOGGED_IN" : [],             
                    " Processor failed: USER_ACTIVATION_INVALID_URL" : [],                       
                    " Processor failed: USER_UPDATE_ERROR_NOT_SAVED_TO_DB" : [],
                    " Processor failed: USER_PASSWORD_RECOVERY_INVALID_URL" : [],
                    " Processor failed: USER_ACTIVATION_SENT_MAIL_FAIL" : []
                },
            ".*(ERROR d.f.i.r.p.AbstractProcessor -)" :
                {              
                    " error message missing. Returning server error." : []                   
                },    
            ".*(ERROR d.f.i.r.j.p.DbcKeyExceptionMapper -)" :
                {
                    " init exception was caught at system border: invalid init token" : []               
                },
            ".*(ERROR d.f.i.r.j.r.a.c.ClientProgramController -)" :
                {
                    " Exception. Error ticket: E-.*" : [],
                    " Exception. Error ticket: E-1" : []                
                }, 
            ".*(ERROR d.f.i.r.syntax.lang.expr.EvalExpr -)" :
                {                   
                    " rule stack: \[expression\]-> line.*" : [],
                    " rule stack: \[expression\]-> line 1:3 at \[\@1,3:3='a',<21>,1:3\]: mismatched input 'a' expecting \{<EOF>, '\?', '\&\&', '\|\|', '==', '!=', '>', '<', '>=', '<=', '%', '\^', '\*', '/', '\+', '\-'\}": [],
                    " rule stack: \[expression, expr\]-> line .*" : []
                    
                 }, 
            ".*(ERROR d.f.i.r.j.r.robot.RobotCommand -)" :
                {
                    " ROBOT_PROTOCOL: robot was already disconnected, when a /pushcmd for token .* terminated. We return a server error" : []
                 },         
            ".*(ERROR d.f.i.r.j.r.a.controller.ClientUser -)" :
                {   
                    " Invalid command: login" : [],
                    " Invalid command: logout" : [],
                    " Exception. Error ticket: E-.*" : []
                 },             
            ".*(ERROR d.f.i.r.persistence.dao.ProgramDao -)" :
                {             
                    " update was requested, timestamps don't match. Has another user updated the program in the meantime\?" : [],
                    " update was requested, but no shared program was found"  : []
                 },      
            ".*(ERROR d.f.i.r.j.p.JAXBProviderFactory -)" :
                {            
                    " marshaller not valid for type com.sun.research.ws.wadl.Application" : []
                 },  
            ".*(ERROR d.f.i.r.r.RobotCommunicator -)" :
                {           
                    " ROBOT_RC: /pushcmd from a robot arrived, no matching state was found - we return a server error" : []
                 },         
            ".*(ERROR d.f.i.r.r.RobotCommunicationData -)" :
                {       
                    " ROBOT_RCD: user approval arrived, but is not expected. State is: WAIT_FOR_PUSH_CMD_FROM_ROBOT. Last request was scheduled .* secs ago": [],
                    " ROBOT_RCD: user approval arrived, but is not expected. State is: ROBOT_IS_BUSY. Last request was scheduled .* secs ago": [],
                    " ROBOT_RCD: user approval arrived, but is not expected. State is: ROBOT_WAITING_FOR_PUSH_FROM_SERVER. Last request was scheduled .* secs ago": [],
                    " ROBOT_RCD: user approval arrived, but is not expected. State is: GARBAGE. Last request was scheduled .* secs ago": [],
                    " ROBOT_RCD: user approval arrived, but is not expected. State is: ROBOT_WAITING_FOR_PUSH_FROM_SERVER. Last request was scheduled .* sec ago": [],
                 },            
            ".*(ERROR d.f.i.r.j.r.a.controller.ClientAdmin -)" : 
                {               
                    " Invalid command: setRobot setting robot name to trSpan": [],
                    " Invalid command: setRobot setting robot name to calliope2020": []
                 },    
            ".*(ERROR d.f.iais.roberta.components.Project -)" :
                {                      
                    " Transformer failed" : [],
                    " Generation of the configuration failed" : []
                 },  
            ".*(ERROR d.f.i.r.j.r.r.RobotDownloadProgram -)" :
                {       
                    " upload error: file '.*.hex' to upload to robot not found."  : []
                 }, 
            ".*(ERROR d.f.i.r.w.CalliopeCompilerWorker -)" :  
                {
                    " compile calliope2016 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, \[1/3\] Building the .*." : [],                         
                    " compile calliope2017 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, \[1/3\] Building the .*." : [],                           
                    " compile calliope2017NoBlue program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, \[1/3\] Building the .*." : []                             
                },                     
                ".*(ERROR d.f.i.r.w.c.ArduinoCompilerWorker -)" :
                { 
                   " compile .* program .* failed with In file included from /tmp/openrobertaTmp/.*.cpp:.*:" : [],
                   " compile .* program .* failed with /tmp/openrobertaTmp/.*.cpp:.*: fatal error: .*.h: No such file or directory" : [],                
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*: In function.*" : [],                   
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.ino: In function 'void setSpeedLeft\(double\)':" : [],                     
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.ino:.*error.*" : [],           
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.ino:.*: error: expected constructor, destructor, or type conversion before '\(' token" : [],
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, In file included from.*"                  : [],
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, In file included from /opt/compiler/avr/avr/include/avr/eeprom.h:.*," : [], 
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, remove .*" : [],                      
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, remove /tmp/openrobertaTmp/.*.a: no such file or directory\)" : [],             
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, lto1: error:.*": [],
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, lto1: error: /tmp/openrobertaTmp/..a: file not recognized"                    : [],    
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, lto1: internal compiler error:.*" : []  ,                 
                   " compile .* program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, lto1: internal compiler error: in read_cgraph_and_symbols, at lto/lto.c:.*" : []
                   
                   
                 },
            ".*(ERROR d.f.i.r.worker.EdisonCompilerWorker -)" :
                {            
                    " compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, ERR: file:.*: Syntax Error, constant 0.0 must be an integer value\)"  : [], 
                    " compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, ERR: file:.*: Syntax error\)"  : [],      
                    " compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, ERR: file:.*: Syntax Error, constant .* is out of range\)"  : [],
                    " compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, ERR: file:.*: Syntax Error, Ed.TuneString only allowed at the top level\)"  : [], 
                    " compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, ERR: file:.*: Syntax Error, COMPARE code too complex for .*.Py\)"  : [],
                    " compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp:.*: error: stray ‘.*’ in program"  : [],
                     " compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, ERR: file:0"  : []                 
                 },

             ".*(ERROR d.f.i.r.w.c.Ev3LejosCompilerWorker -)" :
                {                       
                    " build exception. Messages from the compiler are:" : []
                 },      
             ".*(ERROR d.f.i.r.w.c.Ev3C4ev3CompilerWorker -)" :
                {                       
                    " compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp:.*: error: expected unqualified-id before ‘while’" : [],
                    " compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp:.*: error: stray ‘.*’ in program": [],
                    " compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp: In function ‘void .*\(double\)’:": [],
                    " compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp: In function ‘int main\(\)’:": [],
                    " compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp:.*: warning: \"_GNU_SOURCE\" redefined": [],
                    " compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp: In function ‘void prog\(\)’:": [],
                    " compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.cpp:.*: error: ‘null’ does not name a type; did you mean ‘kill’\?": []
                 },                       
             ".*(ERROR d.f.i.r.worker.NxtCompilerWorker -)" :
                {                     
                    " compile nxt program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, # Error: ';' expected" : [],
                    " compile nxt program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, # Error: Undefined Identifier .*": [],
                    " compile nxt program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, # Error: Undefined Identifier RGB": [],
                    " compile nxt program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, # Error: Unmatched close parenthesis": [],
                    " compile nxt program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, # Error: Math Factor expected": [],
                    " compile nxt program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, # Error: Preprocessor macro function does not match instance \(asm \{ __ReadSensorColorEx\(_port, _colorval, _raw, _norm, _scaled, __RETVAL__\) \}\)": []                  
                 },
             ".*(ERROR d.f.i.r.w.c.SenseboxCompilerWorker -)" :
                {                     
                    " compile sensebox program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.ino: In function 'void loop\(\)':" : [],
                    " compile sensebox program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED, /tmp/openrobertaTmp/.*.ino:.*: error: stray '.*' in program" : []
                 },                   
             ".*(ERROR d.f.i.r.j.r.a.c.ClientConfiguration -)" :
                {                 
                    " Exception. Error ticket: E-.*" : []
                 },
             ".*(ERROR d.f.i.r.w.compile.Bob3CompilerWorker -)" :
                {                  
                    " compile bob3 program .* failed with /tmp/openrobertaTmp/.*.cpp: In function 'void .*\(unsigned int\)':" : []
                 }                     
        }