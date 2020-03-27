# CMPE 148: Lab 1
# Instructions
This program will prompt a user to enter a file and it will read one line from the file and calculate whether each year in the file is a leap year or not. If a file is not found it will exit or if the file data has invalid input (such as a string) then it will let the client know it is invalid. 

 - Steps 
	1. Run both client and server in the terminal 
	2. Client server will prompt user to enter file name or hit enter key to exit
	3. When user enters input, the server will read the line containing the years and calculate to check if it is a leap year or not 
	4. The result will be sent back to the client and then printed onto the screen 
	5. Client can continue entering txt files or exit 

# Files 
- UDP_Server.py
- UDP_Client.py 
- TCP_Server.py 
- TCP_Client.py
- given_test_cases.txt
- invalid_input.txt
- nonLeapYear.txt
- leapyears_only.txt 

# Test Cases
**Test Case 1: given_test_cases.txt**
- Given test cases on lab assignment, it has a mix of leap years and non leap years 
	- Output for UDP/TCP clients: 
  
	`Enter file or hit enter to exit: given_test_cases.txt`
  
	`2000 is a leap year`
  
	`2019 is NOT a leap year`
  
	`2020 is a leap year`
  
	`2021 is NOT a leap year`
  
	`2022 is NOT a leap year`
  
	`2024 is a leap year`
  
	`2100 is a leap year`

**Test Case 2: invalid_input.txt**
- This file does not contain valid input and will give the user an error message 
	- Output on TCP/UDP clients: 
  
		`Enter file or hit enter to exit: invalid_input.txt`
    
		`One or more items in file is not a year` 

**Test Case 3: nonLeapYear.txt**
- Input file with only years that are NOT considered leap years 
	- Output for TCP/UDP clients: 
  
	  `Enter file or hit enter to exit: nonLeapyears.txt`
    
	  `1983 is NOT a leap year`
    
	  `2061 is NOT a leap year`
    
	  `1885 is NOT a leap year`
    
     	  `1817 is NOT a leap year`
      
	  `2027 is NOT a leap year`
	  

**Test Case 4: leapyears_only.txt**
- Input file with only leap years listed 
	- Output TCP/UDP clients: 
  
		`Enter file or hit enter to exit: leapyears_only.txt`
    
		`1976 is a leap year`
    
		`1980 is a leap year`
    
		`1984 is a leap year`
    
		`1988 is a leap year`
    
		`1992 is a leap year`
    
		`1996 is a leap year`

**Test Case 5: User Exit** 
- User input will consist of clicking on the enter key to exit the program. This will stop the client and server connection 
	- Output for TCP/UDP clients: 
  
		`Enter file or hit enter to exit:`
    
		`Samanthas-Air:Lab1 samanthajaime$`
