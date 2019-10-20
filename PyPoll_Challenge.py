import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Counties Options
county_options = []
county_dic= {}
winning_vote=0

# Candidate Options
candidate_options = []
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
total_votes_candidate=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    total_votes_county=0
    for row in file_reader:
        total_votes_county +=1
        county_name = row[1]

        if county_name not in county_options:
            county_options.append(county_name)
            county_dic[county_name]=0
        county_dic[county_name] +=1

        total_votes_candidate += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        
            # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_county:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for  counties in county_dic:
        #counties:key
        county_votes= county_dic.get(counties)
        #print(county_votes)
        vote_percentage= float(county_votes)/float(total_votes_county)*100

        county_results=(
            f"{counties}: {vote_percentage:.1f}% ({county_votes:,})\n")
        print(county_results)
        txt_file.write(county_results) 

    if county_votes > winning_vote:
        winning_vote= county_votes
        winning_county=counties
    largest_turnout= (
    f"\n-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
    print(largest_turnout)  
    txt_file.write(largest_turnout)   

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes_candidate) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_ressults =(
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_ressults)
        txt_file.write(candidate_ressults) 

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary) 
