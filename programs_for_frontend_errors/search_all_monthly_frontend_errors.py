import re
import sys


""" list with errors to ignore """
errors_to_ignore =  [
        "jsToAppInterface >invalid webview type caused by: [object Object]" 
]


def search_client_logger_error_errors(infile, outfile):
    """ for searching of all monthly frontend errors and for noting their line numbers
    :param: infile: .log file with data to  evaluate 
    :param: outfile: output file for the evalation data
    """
    output_file = open(outfile, 'w+')
    with open(infile, 'r') as file: 
        for line_number,line in enumerate(file):
            client_logger_error = re.match(r".*(INFO d.fhg.iais.roberta.util.ClientLogger - log entry: \[\[ERR \]\] \[\[TIME\]\] \d{1,} msec:|INFO d.fhg.iais.roberta.util.ClientLogger - log entry: \[\[ERR \]\]) (.*)", line)
            if client_logger_error is not None:
                if client_logger_error[2] not in errors_to_ignore:
                    output_file.write(str(line_number + 1)+ "::" + client_logger_error[2] + "\n")        
                    continue
                else:
                    continue
            else:
                continue
    output_file.close() 
    

def main():
    """ main function serves for process control 
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
    search_client_logger_error_errors(infile, outfile)    


if __name__ == "__main__":
    main()        