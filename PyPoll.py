# The data we need to retrieve:
#1. Total number of votes cast
#2. A compete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The wineer of the election based on popular vote

import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")

file_to_save = os.path.join("analysis","election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

# winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(election_data)
    
    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking each candidate's votes
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
        

    
    for candidate_name in candidate_options:
        # get the votes of each candidate
        votes = candidate_votes[candidate_name]
        # get the percentage of votes
        vote_percentages = float(votes) / float(total_votes) * 100

    
        #determine which candidate won the election
        if (votes > winning_count) and (vote_percentages > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentages
            winning_candidate = candidate_name
            
        print(f"{candidate_name}: {vote_percentages: .1f}% {votes}\n")


    winning_summary = (
        f"-----------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"Winning Votes: {winning_count}\n"
        f"-----------------"
    )
    
    print(winning_summary)




    