
Folder contains subfolder with programs
→ "extract_monthly_frontend_entries.py": for searching of all monthly frontend entries
→ "extract_and_analyze_frontend_errors.py": for searching and analyzing of frontend errors
→ "known_frontend_errors.py" with known errors, which is used by the program "extract_and_analyze_frontend_errors.py"

How to do the tests
→ each program has its own directory which contains the concrete test files, test instructions and programs
→ Before you run "extract_and_analyze_frontend_errors.py" program you have to run the program "extract_monthly_frontend_entries",because its "test_outfile_frontend_entries.txt" output file is input file of current program
