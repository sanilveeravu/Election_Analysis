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

# 1. Initialize a total vote counter.
total_votes=0

# Candidate Options
candidate_options=[]

# 1. Declare the empty dictionary.
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0


# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    # Read and print the header row.
    headers=next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)

        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name=row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0   

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Print total votes
    print(total_votes)    
    
    # Print candidate names.
    print(candidate_options)

    # Print the candidate vote dictionary.
    print(candidate_votes)

    # To do: perform analysis.
    #print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#outfile=open(file_to_save,"w")

# Write some data to the file.
#outfile.write("Hello World")
with open(file_to_save,"w") as txt_file:
    # txt_file.write("Counties in the current election\n")
    # txt_file.write("--------------------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")

    # Print the final vote count to the terminal.
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results,end="")
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        vote_percentage=float(candidate_votes[candidate_name])/float(total_votes)*100
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if candidate_votes[candidate_name] > winning_count:
            winning_candidate=candidate_name
            winning_count=candidate_votes[candidate_name]
            winning_percentage=float(candidate_votes[candidate_name])/float(total_votes)*100
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.   
        candidate_results=f"{candidate_name}: {vote_percentage:.1f}% ({candidate_votes[candidate_name]})\n"
        print(candidate_results)
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"-------------------------\n"
    )

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


# Close the file
#outfile.close()
