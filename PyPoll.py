# Data to retrieve 
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import datetime as dt
import csv 
import os 

now = dt.datetime.now()
print("the time right now is :" , now)

# Assign a variable for the file to load and the path.
#file_to_load = "Resources/election_results.csv"
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file.
election_data = open(file_to_load,"r")

# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    # Read and print the header row.
    headers=next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

    # To do: perform analysis.
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#outfile=open(file_to_save,"w")

# Write some data to the file.
#outfile.write("Hello World")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the current election\n")
    txt_file.write("--------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()
