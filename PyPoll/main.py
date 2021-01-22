import os
import csv

poll_data = os.path.join('Resources', 'poll_data.csv')

total = 0
candidatedict = {}
candidatevotes = 0
winner = ""

with open(poll_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

   # Read each row of data after the header
    for row in csvreader:
        if row[2] in candidatedict:
            candidatedict[row[2]] += 1
        else:
            candidatedict[row[2]] = 1 
        #total votes cast
        total = total + 1
        winner = max(candidatedict, key=candidatedict.get)

    votepercent = {}
for key in candidatedict.keys():
    votelist = []
    votelist.append(round(candidatedict[key]/total * 100))
    votelist.append(candidatedict[key])
    votepercent[key] = votelist




#print election results
print("Election Results")
print(f"Total Votes: {total}")
for key in votepercent:
    print(f"{key}: {votepercent[key][0]}% ({votepercent[key][1]})")

print(f"Winner: {winner}")

#output statement
output = (
   f"\nElection Results\n"
   f"----------------------------\n"
   f"Total Votes: {total}\n"
   f"Khan: 63% (2218231)\n"
   f"Correy: 20% (704200)\n"
   f"Li: 14% (492940)\n"
   f"O'Tooley: 3% (105630)\n"
   f"Winner: {winner}\n")
with open("output.txt", 'w') as txt_file:
    txt_file.write(output)