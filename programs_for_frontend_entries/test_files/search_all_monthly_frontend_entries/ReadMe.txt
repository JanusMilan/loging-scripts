How to run a program in the console: 
→ python3 search_all_monthly_frontend_entries.py test_infile_frontend_entries.txt test_outfile_frontend_entries.txt

Test input file
→input file "test_infile_frontend_entries.txt" has 10 lines
→line 1 is Frontend [INFO] entry which is to be ignored 
→line 2 is Frontend [INFO] entry which is to be ignored 
→lines 3 and 4 are Frontend [INFO] entries which are not to be ignored and are part of the output file
→line 5 is Frontend [ERROR] entry which is to be ignored 
→lines 6 and 7 are Frontend [ERROR] entries which are not to be ignored and are part of the output file
→line 8 is Frontend [TIME] which entry is not to be ignored and it is part of the output file
→lines 9 and 10 are Backend [ERROR] entries which are to be ignored
	
Evaluation of the test
→5 of 10 entries from input file are to be ignored 
→output file hat 5 lines with the right entries, what is correct
→the correct line number appears before each message
