#Import Modules/Dependencies
import os
import csv

# Path of CSV
csvpath = os.path.join('..', "Resources", "bankcsv.csv")


#Open & Read CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)

 #Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
increase = 0
increase_month = 0
decrease = 0
gdecrease_month = 0  
#Calculate Number Of Months & Net Amount
previous_row = int(row[1])
total_months += 1
net_amount += int(row[1])
increase = int(row[1])
increase_month = row[0]   