import re
import sys
  

def search_client_logger_error_errors(infile, outfile):
    """ search for types of frontend errors 
    :param: infile: .log file with data to  evaluate 
    :param: outfile: output file for the evalation data
    """
    error_types_dict = dict()
    with open(infile, 'r') as file: 
        for row in file:
            client_logger_error = re.search(r"(INFO d.fhg.iais.roberta.util.ClientLogger - log entry: \[\[ERR \]\] \[\[TIME\]\]|INFO d.fhg.iais.roberta.util.ClientLogger - log entry: \[\[ERR \]\]) \d{0,5} msec: (.*)", row)
            if client_logger_error is not None:
                error_types_dict.update({client_logger_error[2]: client_logger_error[2]})
                # print(client_logger_error[2])
                continue
            else:
                continue                            
    with open(outfile, 'w') as file: 
        for element in error_types_dict:
            file.write(element + "\n")
            
            
def main():
    """ main function serves for process control """
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
    search_client_logger_error_errors(infile, outfile)    
    

if __name__ == "__main__":
    main()        