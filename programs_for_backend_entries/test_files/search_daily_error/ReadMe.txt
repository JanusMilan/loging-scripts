
################ Programm search_daily_errors.py ################ 
General information about the program
→ Any monthly log file is analyzed 
→ Log file contains the messages for server start (by default at 03:00)
→ The program loads all ERROR LOG lines for the whole day, when the day to be checked is entered interactively
→ Sketch of the program:
  → The program is started with the month and day being checked 	
  → Program loads log file for the month to be checked
  → The log file looks for a message for server start on the specified date
  → All LOG ERROR messages for this day are searched until the next Sarver start and output to a file 
