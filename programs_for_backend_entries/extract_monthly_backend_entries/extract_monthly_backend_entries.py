import re
import sys


""" list with lines to ignore """
lines_to_ignore =  [
        r".*d.fhg.iais.roberta.util.ClientLogger.*",
        r".*d.f.i.r.c.AbstractCompilerWorkflow.*"
]


client_log_pattern = [
    r".*(.*INFO d.f.i.r.p.AbstractProcessor - Processor failed:) (.*)",
    r".*(.*ERROR d.f.i.r.p.AbstractProcessor) (.*)",  
    r".*(.*ERROR d.f.i.r.j.p.DbcKeyExceptionMapper - init exception was caught at system border:) (.*)",
    r".*(.*ERROR d.f.i.r.j.r.a.c.ClientProgramController - Exception.) (.*)",        
    r".*(.*ERROR d.f.i.r.syntax.lang.expr.EvalExpr - rule stack:) (.*)",        
    r".*(.*ERROR d.f.i.r.j.r.robot.RobotCommand - ROBOT_PROTOCOL:) (.*)",        
    r".*(.*ERROR d.f.i.r.j.r.a.controller.ClientUser) (.*)",        
    r".*(.*ERROR d.f.i.r.persistence.dao.ProgramDao) (.*)",        
    r".*(.*ERROR d.f.i.r.j.p.JAXBProviderFactory) (.*)",        
    r".*(.*ERROR d.f.i.r.r.RobotCommunicator) (.*)",        
    r".*(.*ERROR d.f.i.r.r.RobotCommunicationData - ROBOT_RCD: user approval arrived, but is not expected. State is:) (.*)",        
    r".*(.*ERROR d.f.i.r.j.r.a.controller.ClientAdmin - Invalid command:) (.*)",        
    r".*(.*ERROR d.f.iais.roberta.components.Project) (.*)",        
    r".*(.*ERROR d.f.i.r.j.r.r.RobotDownloadProgram) (.*)",        
    r".*(.*ERROR d.f.i.r.w.CalliopeCompilerWorker - compile calliope2016 program .* failed with) (.*)", 
    r".*(.*ERROR d.f.i.r.w.CalliopeCompilerWorker - compile calliope2017 program .* failed with) (.*)",            
    r".*(.*ERROR d.f.i.r.w.CalliopeCompilerWorker - compile calliope2017NoBlue program .* failed with) (.*)",            
    r".*(.*ERROR d.f.i.r.w.c.ArduinoCompilerWorker - compile .* program .* failed with) (.*)",            
    r".*(.*ERROR d.f.i.r.worker.EdisonCompilerWorker - compile edison program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED,) (.*)",   
    r".*(.*ERROR d.f.i.r.w.c.Ev3LejosCompilerWorker - build exception.) (.*)",   
    r".*(.*ERROR d.f.i.r.w.c.Ev3C4ev3CompilerWorker - compile ev3c4ev3 program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED,) (.*)",   
    r".*(.*ERROR d.f.i.r.worker.NxtCompilerWorker - compile nxt program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED,) (.*)",   
    r".*(.*ERROR d.f.i.r.w.c.SenseboxCompilerWorker - compile sensebox program .* failed with \(COMPILERWORKFLOW_ERROR_PROGRAM_COMPILE_FAILED,) (.*)",  
    r".*(.*ERROR d.f.i.r.j.r.a.c.ClientConfiguration - Exception.) (.*)",     
    r".*(.*ERROR d.f.i.r.w.compile.Bob3CompilerWorker - compile bob3 program .* failed with) (.*)"                                
]

    
def filter_log_lines(infile, outfile):
    """ read all log lines from a file, write the lines, that are
    - client lines and
    - do not match one of the pattern defined in lines_to_ignore
    :param: infile: file with all log lines
    :param: outfile: file with the filtered data
    """
    date = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    client_log_pattern_regex = []
    for pattern in client_log_pattern:
        client_log_pattern_regex.append(re.compile(date +  pattern))  
    lines_to_ignore_regex = []
    for line_to_ignore in lines_to_ignore:
        lines_to_ignore_regex.append(re.compile(line_to_ignore))
    with open(outfile, 'w+') as output_file:
        with open(infile, 'r') as input_file:  
            for line_number,line in enumerate(input_file):
                for regex in client_log_pattern_regex:
                    client_logger_line = regex.match(line)
                    if client_logger_line is not None:
                        for regex in lines_to_ignore_regex: 
                            if regex.match(line) is not None:     
                                break
                        else:        
                            output_file.write('{:08d}!!!!!{:s}: {:s} {:s}\n'.format(line_number + 1,client_logger_line[1],client_logger_line[2],client_logger_line[3]))
  
  
def main():
    try:
        filter_log_lines(sys.argv[1], sys.argv[2])  
    except IndexError:
        sys.exit("usage: extract_monthly_frontend_entries <infile> <outfile>") 


if __name__ == "__main__":
    main()        
