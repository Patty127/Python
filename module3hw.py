#!/usr/bin/python3

# Homework 3 part 1 - Solution
#   Conditional if elif
#   If the number is 7 then the program should print "seven",
#   If the number is 9 then the program should print "nine",
#   If the number is 1 then the program should print "one", 
#   If the number is 10 then the program should print "ten", 
#   If the number is 5 then the program should print "five", 
#   Otherwise, your program should print "unknown number".

nmbr=input("Please enter an integer number:")
checkin_nmbr= int(nmbr)
if checkin_nmbr==7:
    print("seven")
elif checkin_nmbr== 9:
    print("nine")
elif checkin_nmbr == 1:
    print("one")
elif checkin_nmbr == 10:
    print("ten")    
elif checkin_nmbr == 5:
    print("five")
else:
    print("unknown number")

# Homework 3 part 2 - Solution
# Converting input to a string and catching an error if any
nmbr = input("Please enter anything here ")
try:
    nmbr = int(nmbr)
except ValueError:
    print('Error')
else:
    print(nmbr)