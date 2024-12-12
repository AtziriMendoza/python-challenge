# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(r"C:\Users\luzch\Data Science Boot Camp\NU-VIRT-DATA-PT-10-2024-U-LOLC\python-challenge\Starter_Code\PyPoll\Resources\election_data.csv")  # Input file path
file_to_output = os.path.join(r"C:\Users\luzch\Data Science Boot Camp\NU-VIRT-DATA-PT-10-2024-U-LOLC\python-challenge\Starter_Code\PyPoll\analysis\.gitkeep")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
max_percentage_votes = 0 #percentage of votes each candidate won
votes_per_candidate = 0 #total number of votes each candidate won
election_winner = "" #the winner of the election based on popular vote


# Define lists and dictionaries to track candidate names and vote counts
candidate_list = [] #list of candidates w/ votes
candidates_and_votes = {} #how do I make the candidates name the key and the vote count is the value?
candidate_percentage = {}
# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    #reader = csv.reader(election_data)- can't open the file twice
    csv_dict_reader = csv.DictReader(election_data) 

    # Skip the header row
    #header = next(reader)

    # Loop through each row of the dataset and process it
    for row in csv_dict_reader:

    # print(candidate_list)
    # print(candidates_and_votes)
    # print(total_votes)- had to print this statement outside of the loop

#WHAT DO i NEED TO DO:
        #need to extract the candidate's name from row[2]
        #for each row, increment the total number of votes (total_votes)
        #for each candidate, increment their vote count in a dictionary

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1
        

        # Get the candidate's name from the row
        candidate_name = row["Candidate"] #gets the candidate's name from the row- assumes column name is "Candidate")

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

        # Add a vote to the candidate's count
        if candidate_name not in candidates_and_votes:
            candidates_and_votes[candidate_name] = 1 #initialize vote count for new candidate
        else:
            candidates_and_votes[candidate_name] += 1 #increment vote count for existing candidate

# Open a text file to save the output
    output= (
        f"Election Results\n"
        f"---------------\n"    
        f"Total Vote Count: {total_votes}\n"
        f"---------------\n"
    )
    #print(output)
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidates_and_votes.items(): #this is a new loop
        percentage_votes = (votes/ total_votes)*100
        candidate_percentage[candidate] = percentage_votes
#print(percentage_votes)
# print(candidate_percentage)

for candidate, percent in candidate_percentage.items():
    if percent > max_percentage_votes:
        max_percentage_votes = percent
        election_winner = candidate 
            #election_winner = max(candidate_percentage, key=candidate_percentage.get)
            #we are getting the max key values in the dictionary, have to use the key 
            #item so that the max item is applied to every item in the dictionary to determine which item is the max
            #candidate_percentage.get retrieves the value associated with each key in the dictionary
#print(election_winner)
for candidate in candidate_percentage:
    votes = candidates_and_votes[candidate]
    percentage_votes = candidate_percentage[candidate]
    # Print and save each candidate's vote count and percentage
    output += (
        f"{candidate}: {percentage_votes:.2f}% ({(votes)})\n"
        )
output += (
    f"---------------\n"
    f"Winner: {election_winner}\n"
    f"---------------\n"
    )
print(output)
    # Print the total vote count (to terminal)
with open(file_to_output, "w") as txt_file:
    # Write the total vote count to the text file
    txt_file.write(output)