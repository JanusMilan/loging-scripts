import re
import sys
from enum import Enum


""" list with lines to ignore """
lines_to_ignore =  [
        ".*jsToAppInterface >invalid webview type caused by: \[object Object\]",
        ".*init .* view",
        ".*init .* delete",
        ".*no Android Webview.*",
        ".*no IOS Webview.*"
]

def filter_log_lines(infile, outfile):
    """ read all log lines from a file, write the lines, that are
    - client lines and
    - do not match one of the pattern defined in lines_to_ignore
    :param: infile: file with all log lines
    :param: outfile: file with the filtered data
    """
    client_log_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*(INFO d.fhg.iais.roberta.util.ClientLogger - log entry: (\[\[ERR \]\] \[\[TIME\]\] .* msec:|\[\[TIME\]\] .* msec:|\[\[ERR \]\]|\[\[INFO\]\])) (.*)"
    client_log_pattern_regex = re.compile(client_log_pattern)
    lines_to_ignore_regex = []
    for line_to_ignore in lines_to_ignore:
        lines_to_ignore_regex.append(re.compile(line_to_ignore))

    with open(outfile, 'w+') as output_file:
        with open(infile, 'r') as input_file:  
            for line_number,line in enumerate(input_file):
                client_logger_line = client_log_pattern_regex.match(line)
                if client_logger_line is not None:
                    for regex in lines_to_ignore_regex: 
                        if regex.match(line) is not None:     
                            break
                    else:                    
                        output_file.write('{:08d}::{:s}: {:s} {:s}\n'.format(line_number + 1,client_logger_line[1],client_logger_line[3],client_logger_line[4]))
        
def main():
    try:
        filter_log_lines(sys.argv[1], sys.argv[2])  
    except IndexError:
        sys.exit("usage: extract_monthly_frontend_entries <infile> <outfile>") 

if __name__ == "__main__":
    main()        
