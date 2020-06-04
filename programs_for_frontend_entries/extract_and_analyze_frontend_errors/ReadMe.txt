How to test program
→ Before you run this program you have to run the program "extract_monthly_frontend_entries", 
    → because its "test_outfile_frontend_entries.txt" output file is input file of current program
→python3 extract_and_analyze_frontend_errors.py test_outfile_frontend_entries.txt test_outfile_frontend_errors.txt 


Test input file
→There are 3 [[INFO]] lines with 2 different types of entries, these should not appear in the output file
	→Entry: "runOnBrick from blockly button" with one line
	→Entry: ". * Init gui state" with two lines
→There are 12 [[ERR ]] [[TIME]] lines with 2 so far known different types, these should appear in the output file
	→Entry ". * Out of memory" with ten lines
	→Entry ". * TypeError: Cannot read property 'selector' of undefined" with two lines	
→There are is 1 [[TIME ]] entriy, these should not appear in the output file
→Entry "tabConfiguration clicked" with one line
→There are 2 [[ERR ]] lines with 2 so far known different types
	→Entry "Client connection issue: 0"	with one line
	→Entry "Client connection issue: 200" with one line	
→There are 3 [[ERR ]] [[TIME]] lines with 2 so far unknown different types, these should appear in the output file
	→Entry "simScene clicked, then EXCEPTION: TypeError: robots [0] is undefined" with two lines
	→Entry "simScene clicked, then EXCEPTION: TypeError: undefined is not an object (evaluating 'robots [0] .debug')" with one lines	
→1 previously unknown [[ERR ]] line with 1 so far unknown type, these should appear in the output file 
	→Entry "Client connection issue: 460"	


Evaluation of the Test output file
→a total of 7 [[ERR]] [[TIME]] ​​and [[ERR]] entry types should appear
	→4 previously known
	→3 previously unknown


	
	