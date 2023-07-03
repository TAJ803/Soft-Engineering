year = int(input("Enter a year: "))
#
# Write your code here.
#	
if year <= 1581:            # calculating if year entered before 1582
    print("Not within the Gregorian calendar period")
    exit()

####
if year % 4 != 0:                   #year not exactly divisible by 4
    print("Its a common year")
elif year % 100 != 0:               #year not exactly divisible by 100
    print("Its a leap year")
elif year % 400 != 0:               #year not exactly divisible by 400
    print("Its a common year")
else:
    print("Its a leap year")