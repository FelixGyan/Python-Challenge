#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv
file_data=r'D:\2023\Training\Data Analysis\USA\Challenge no 3\Challenge 3 budget data.csv'


# Define the file path
csvpath = os.path.join(file_data)

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
dates = []

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        # Extract data from the current row
        date = row[0]
        profit = int(row[1])

        # Calculate the total number of months and net total
        total_months += 1
        net_total += profit

        # Calculate profit change and store in the list
        if total_months > 1:
            change = profit - previous_profit
            profit_changes.append(change)
            dates.append(date)

        previous_profit = profit

# Calculate the average change
average_change = sum(profit_changes) / len(profit_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Get the corresponding dates for the greatest increase and decrease
greatest_increase_date = dates[profit_changes.index(greatest_increase)]
greatest_decrease_date = dates[profit_changes.index(greatest_decrease)]

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Close the text file
textfile.close()


# In[ ]:




