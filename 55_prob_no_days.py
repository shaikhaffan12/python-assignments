from datetime import date, datetime

first_date = input("Enter First Date: ")
last_date = input("Enter last Date: ")

# Convert input string To Date
f_d = datetime.strptime(first_date, "%d/%M/%Y").date() 
l_d = datetime.strptime(last_date, "%d/%M/%Y").date()

# find Difference Between Dates
diff = l_d - f_d

print(diff.days)