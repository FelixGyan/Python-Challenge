#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

 

 
file_data=r'D:\2023\Training\Data Analysis\USA\Challenge no 3\challenge 3 election_data.csv'
# Define the file path
csvpath = os.path.join(file_data)

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        # Extract data from the current row
        voter_id = row[0]
        candidate = row[2]

        # Count the total number of votes
        total_votes += 1

        # Count the votes for each candidate
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Calculate the percentage of votes each candidate won and find the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = "election_results.txt"
with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")

# Close the text file
textfile.close()


# In[ ]:




