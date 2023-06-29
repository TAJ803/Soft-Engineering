hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
total_mins = mins + dura #additing mins and duration to get total mins
convert_mins_into_hrs = total_mins // 60    # converting total mins into hours
total_hours = hour + convert_mins_into_hrs  # adding input hour + calculated hours in step 7

# applying modules on mins and hrs, which mean anything over 60 or 24 will call forward
total_mins = total_mins % 60
total_hours = total_hours % 24

print(total_hours, ":", total_mins) #printing final output