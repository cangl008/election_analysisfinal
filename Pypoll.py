
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes=0
# Using the open() function with the "w" mode we will write data to the file
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) 
 # Read and print the header row.
    headers = next(file_reader)
    for row in file_reader:
       total_votes +=1
print(total_votes)
    

     

# To do: perform analysis.
print(election_data)

#CLose the file.
election_data.close()

# 1. The total number of votes cast
# 2. A complete list of candidates
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candiates won
# 5. The winner of the election based on popular vote.
