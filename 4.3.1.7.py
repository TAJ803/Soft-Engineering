def is_year_leap(year):
#
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
#
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
##########################################################
def days_in_month(year, month):
#
    days = 0
    months_with_31_days = [1,3,7,5,8,10,12]
    if year % 4 == 0 :              
        days = 1
        if year % 100 == 0 :
            days = 0
        if year % 400 == 0 :
            days = 1
    if month == 2 :
        return 28 + days
    if month in months_with_31_days :
        return 31
    return 30
#
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
