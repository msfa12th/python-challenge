#  Python-Challenge
#  PyBank
#  main.py
#  
#  author: Mary Brown
#  date created: 8/24/2019
#
#  a Python script for analyzing simple financial records for the company
#  source file: (PyBank/Resources/budget_data.csv)
#       The dataset is composed of two columns: `Date` and `Profit/Losses`. 

# utilize tools for csv
import os
import csv
import sys

# initialize variables
dates = []
profits = []
profitChanges = []

totalMonths = 0
totalProfit = 0

netChange = 0
numChanges = 0
avgChange = 0
minProfitChange = 0
maxProfitChange = 0

#read in raw data
budget_csv = os.path.join("Resources","budget_data.csv")

# open the file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)  # skip the headers

    for row in csvreader:
        totalMonths = totalMonths + 1 
        totalProfit = totalProfit + int(row[1])   
        dates.append(row[0])
        profits.append(int(row[1]))

# done reading file, do calculations        
for i in range(totalMonths):
    if i > 0:
        profitChanges.append(profits[i] - profits[i-1])
        netChange = netChange + profits[i] - profits[i-1]
        numChanges = numChanges + 1

avgProfitChange = netChange/numChanges
minProfitChange = min(profitChanges)
maxProfitChange = max(profitChanges)

for i in range(numChanges):
    if profitChanges[i] == minProfitChange:
        minProfitChangeMonth = dates[i+1]

    if profitChanges[i] == maxProfitChange:
        maxProfitChangeMonth = dates[i+1]

# 1st print results
print("   ")
print("Financial Analysis")
print("---------------------------------------------")
print(f'Total Months: {totalMonths}')
print(f'Total: ${totalProfit}')
print('Average Change: ${:.2f}'.format(avgProfitChange))
print(f'Greatest Increase in Profits: {maxProfitChangeMonth} (${maxProfitChange})')
print(f'Greatest Decrease in Profits: {minProfitChangeMonth} (${minProfitChange})')
print("  ")

# 2nd print result to file
filename  = open("output.txt",'w')
sys.stdout = filename

print("   ")
print("Financial Analysis")
print("---------------------------------------------")
print(f'Total Months: {totalMonths}')
print(f'Total: ${totalProfit}')
print('Average Change: ${:.2f}'.format(avgProfitChange))
print(f'Greatest Increase in Profits: {maxProfitChangeMonth} (${maxProfitChange})')
print(f'Greatest Decrease in Profits: {minProfitChangeMonth} (${minProfitChange})')
print("  ")

