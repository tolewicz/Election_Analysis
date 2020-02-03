#import key modules
import csv
import os


# defining initial varaibles and empty objects
total_votes = 0
candidate_list = []
candidate_votes = {}
county_list = []
county_poll = {}
candidate_county_votes = {}
winning_candidate = ""
winning_votes = 0
winning_percentage = 0
winning_county = ""
cwinning_votes = 0
cwinning_percentage = 0



# calling path to election results file
csvpath_to_read = os.path.join('..','Election_Analysis','election_results.csv')

#opening the file and assigning is as variable
with open(csvpath_to_read) as file_to_read:
    file_to_read = csv.reader(file_to_read)
    headder = next(file_to_read) 


#iterate over rows and get data from each row to count total votes
    for row in file_to_read:
        total_votes +=1

        #identyfying candidate name and county name while reading each row
        candidate_name = row[2]
        county_name = row[1]

        
        #creating list of candidates (per challenge request)
        #using dictionaries to calcualte the number of votes
        
        #Removed list creating loop
        #if candidate_name not in candidate_list:
         #   candidate_list.append(candidate_name)
        if candidate_name not in candidate_votes:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #adding +1 vote to candidate name
        candidate_votes[candidate_name] +=1

        #creating list (per challenge request) and calculating total votes per county
        if county_name not in county_list:
            county_list.append(county_name)
            county_poll[county_name] = 0
        county_poll[county_name] += 1
    print(county_poll)


#opening a text file to save results
file_to_save = os.path.join('..','Election_Analysis', 'election_analysis.txt')
with open(file_to_save, "w") as txt_file:

#printing # of total votes in terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results)
    # Save the final vote count to the text file.
    txt_file.write(election_results)

#County turnout
##counting number and percentage of votes
    for county_name in county_poll:
        cvotes = county_poll[county_name]
        cvote_percentage = (float(cvotes)/float(total_votes))*100
        county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        
        ## determining the county with largest turnout
        if (cvotes > cwinning_votes) and (cvote_percentage > cwinning_percentage):
            cwinning_votes = cvotes
            cwinning_percentage = cvote_percentage
            winning_county = county_name

    ## printing results
    winning_county_summary = (f"----------------------------------------------- \n"
                                f"Largest County Turnout: {winning_county} \n"
                                f"----------------------------------------------- \n")
    ##saving results to text file
    print(winning_county_summary)
    txt_file.write(winning_county_summary)

# candidate winner
## counting number and percentage of votes
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes)/float(total_votes))*100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
        ##determinig candidate with largest number and percentage of votes
        if (votes > winning_votes) and (vote_percentage > winning_percentage):
            winning_votes = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    ##printing results
    winning_candidate_summary = (f"----------------------------------------------- \n"
                                 f"Winner: {winning_candidate} \n"
                                 f"Winning vote count: {winning_votes:,}\n"
                                 f"Winning percentage: {winning_percentage:.1f}\n"
                                 f"----------------------------------------------- \n")
    ##saving results to text file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
