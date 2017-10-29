# -*- coding: UTF-8 -*-
"""PyPoll Code."""

#import modules needed
import os
import csv


#set read and write paths
path_to_read = "./raw_data"
path_to_write = "./output"

#get csv file names to process from input directory
files_to_process = []
for file in os.listdir(path_to_read):
    if file.endswith(".csv"):
        files_to_process.append(file)
# print(files_to_process)


#Loop through each file to process
for file in files_to_process:
    #init dictionary 
    candidate_vote_counts = {}

    #set path to read file from
    file_to_read = os.path.join(path_to_read, file)

    #open file and read via dictionary object
    with open(file_to_read, 'r') as csvFile:
        dict_reader = csv.DictReader(csvFile)
        #Loop through dictionary list and set up
        #dictionary with candidate as key and vote count as value
        for row in dict_reader:
            #set count = 1 if first vote for candidate else incr by 1
            if row["Candidate"] in candidate_vote_counts:
                candidate_vote_counts[row["Candidate"]] += 1
            else:
                candidate_vote_counts[row["Candidate"]] = 1

    # sum values to get total vote count
    total_votes = sum(candidate_vote_counts.values())
    # get key for maximun value
    maximum_key = max(candidate_vote_counts, key=candidate_vote_counts.get)
    # get value for the maximun key
    maximum_value = candidate_vote_counts[maximum_key]

    #print to console
    print("\n"+"="*50)
    print(f"\nElection Results for {file}")
    print("\n"+"="*50)
    print(f"Total Votes: {total_votes}")
    print("="*50)
    
    for candidate in candidate_vote_counts.keys():
        print(f"{candidate}: " + " {:.1%}".format(candidate_vote_counts[candidate]/total_votes) + f"({candidate_vote_counts[candidate]})")
    print("="*50)
    print(f"Winner : {maximum_key}")
    print("="*50)


    # Open file in output directory and print output to file
    file_to_write = os.path.join(path_to_write, (file.split("."))[0] + ".txt")
    with open(file_to_write, 'w') as filewriter:

        print("\n"+"="*50 ,file=filewriter)
        print(f"\nElection Results ", file=filewriter)
        print("\n"+"="*50,file=filewriter)
        print(f"Total Votes: {total_votes}",file=filewriter)
        print("="*50,file=filewriter)
    
        for candidate in candidate_vote_counts.keys():
            print(f"{candidate}: " + " {:.1%}".format(candidate_vote_counts[candidate]/total_votes) + f"({candidate_vote_counts[candidate]})",file=filewriter)
        print("="*50,file=filewriter)
        print(f"Winner : {maximum_key}",file=filewriter)
        print("="*50,file=filewriter)

