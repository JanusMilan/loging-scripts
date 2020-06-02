
how to run program in the console: 
--> python3 search_all_monthly_frontend_errors.py test_infile_frontend_error.txt front_end_error_file.txt 

evaluation of the test
--> input file "test_infile_frontend_error.txt" has 131 lines
	--> one line (1. line) with error "jsToAppInterface >invalid webview type caused by" which is in evaluation to ignore 
	--> 8 lines with non-error entry "[[TIME]] 89 msec: tabConfiguration clicked"
    --> so output file should have 122 with error entries\lines 
--> output file 
	--> has 122 error entries\lines 
    --> the correct line number appears before each message
--> test is successful