import os
import csv

# Set Variables
month = 0
monthchange = []
netchangelist = []
increase = ["", 0]
decrease = ["", 0]
net = 0

#load and read csv file
budget_data = os.path.join('Resources', 'budget_data.csv')
with open(budget_data, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

# Split data 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    row = next(csvreader)
    month = month + 1
    net = net + int(row[1])
    previousnet = int(row[1])

    # Loop to read each row and calculate 
    for row in csvreader:
        month = month + 1
        net = net + int(row[1])
        netchange = int(row[1]) - previousnet
        previousnet = int(row[1])
        netchangelist = netchangelist + [netchange]
        monthchange = monthchange + [row[0]]
        if netchange > increase[1]:
            increase[0] = row[0]
            increase[1] = netchange
        if netchange < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = netchange

monthlyaverage = (sum(netchangelist)/len(netchangelist))
monthlyaverage = str(round(monthlyaverage, 2))

# Print
print("Financial Analysis")
print(f"Total Months: {month}")
print(f"Total: ${net}")
print(f"Average Change: ${monthlyaverage}")
print(f"Greatest Increase in Profits: {increase[0]} (${increase[1]})")
print(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})")

# Write new file!!
output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {month}\n"
   f"Total: ${net}\n"
   f"Average  Change: ${monthlyaverage}\n"
   f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
   f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n")
with open("output.txt", 'w') as txt_file:
    txt_file.write(output)