import re
import sys


def write_output(outfile, lines_to_check, thread_id):
    """ for write the output file 
        :param: outfile: output file
        :param: lines_to_check: lists with lines of candidates that could be related to wanted thread (with error)        
        :param: thread_id: wanted thread, which should be examined        
    """
    with open(outfile, 'w+') as output_file:
        for line in lines_to_check:
            if re.search(thread_id, line) is not None:
                output_file.write(line)                
                
    
def find_thread(infile, outfile, error_line_number):
    """ for searching the messages which are related to thread from the given line number 
        :param: infile: log file for analysis 
        :param: outfile: output file
        :param: error_line_number: line number with error, whose context lines have to be filtered out        
    """    
    thread_id_regex = re.compile(r"(qtp917819120-\d{0,4})")
    lines_to_check = []
    if error_line_number >= 10:
        start_position_to_check = error_line_number - 10
        end_position_to_check = error_line_number + 10
    else: 
        start_position_to_check = 0
        end_position_to_check = 10  
    with open(infile, 'r') as input_file:  
        for line_number,line in enumerate(input_file):
                line_number = line_number + 1
                if line_number < start_position_to_check:
                    continue
                elif line_number >= start_position_to_check and line_number < error_line_number:
                    lines_to_check.append(line)
                elif line_number == error_line_number:
                    thread_id_match = thread_id_regex.search(line)
                    if thread_id_match is not None:                            
                        thread_id = thread_id_match.group(1)
                        lines_to_check.append(line)
                    else:
                        raise Exception('This line has no thread specification. This line number was given: {}'.format(error_line_number))  
                elif error_line_number < line_number and line_number <= end_position_to_check:           
                    lines_to_check.append(line)                            
                else:
                    print() 
                    return write_output(outfile, lines_to_check, thread_id)      
  
def main():
    """ main function serves for process control    
    """        
    try:
        find_thread(sys.argv[1], sys.argv[2], int(sys.argv[3]))  
    except IndexError:
        sys.exit("usage: find_and_print_thread_entries.py <infile> <outfile> <error_line_number>") 


if __name__ == "__main__":
    main()        
