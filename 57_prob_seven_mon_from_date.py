from datetime import date,datetime
from dateutil.relativedelta import relativedelta

# get Date From console 
f_date = input("Enter From Date: ")
f_d = datetime.strptime(f_date, "%d/%M/%Y").date() 

# use relativedelta package for finding date of next seven month
six_m = f_d + relativedelta(months =+ 7)

print(six_m)