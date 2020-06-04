Allgemeines zum Programm
→ There is a monthly log file 
→ Among other things, the log file also contains the messages for server start
→ A maximum of 4 lines later there is corresponding message that user programs are loaded
→ Program checks whether server start is regular and regular
→ Sketch of the program:
  → Program loads log file and evaluates it
  → Searching for server start message
  → Then the related message "..Number of programs stored .." is searched
  → Both messages are evaluated in the "evaluate_server_start_entry" function
     → Check whether the server started as scheduled at 03:00
     → Check whether the user programs are loaded after server start
     → After evaluating the program, the result is output in an output file
      → Possible results (depending on the case) are: 	 
	→ Server started on schedule and programs are loaded 
        → Server did NOT start on schedule and programs are loaded 
        → Server started on schedule and programs are NOT loaded 			
	→ Server did NOT start on schedule and programs are NOT loaded 	
  → Further messages for server start are successively searched until the EOF
  → When all messages for server start are recorded in the log file
    → Then output file is evaluated in function "evaluate_server_starts", 
    → whether all Sertver Start are regular or there are ERRORS
    → The corresponding message is attached to the EOF in the output file	
		 
To test programm from folder with program "search_server_error.py" 
→ go to folder: "cd test_files/search_server_error/"
→ Start the programm in the console: "python3 ../../search_server_error.py  test_input.txt  test_output.txt"

OR put test files together with program file in the same folder
→ Start the programm in the console: "python3 search_server_error.py  test_input.txt  test_output.txt"
