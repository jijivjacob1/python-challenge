# -*- coding: UTF-8 -*-
"""PyBoss Code."""

#import modules needed
import os
import csv
from datetime import datetime

#get csv file names to process from input directory
files_to_process = []
path_to_read = "./raw_data"
path_to_output = "./output"
for file in os.listdir(path_to_read):
    if file.endswith(".csv"):
        files_to_process.append(file)
#print(files_to_process)


"""Returb State Abbreviation for Input State Name."""
def get_state_abbrev(state_name):

    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

    return us_state_abbrev[state_name]

"""Parse SSN and return encrypted value"""
def encrpty_ssn(ssn):

    ssn_split = ssn.split("-")

    return ('*' * len(ssn_split[0])) + '-' + ('*' * len(ssn_split[1])) + '-' + ssn_split[2]

  
#Loop through each file to process
for file in files_to_process:
     # Set empty list variables
    id_emp = []
    nm_first = []
    nm_last = []
    dob = []
    ssn = []
    state = []
    
   
    #set path to read file from
    file_to_read = os.path.join(path_to_read, file)

    # Create new CSV
    newemployeeCSV = os.path.join(path_to_output, 'employee_date-' + str(datetime.today().strftime("%Y-%m-%d %H:%M")) + '.csv')


    # Open current wrestling CSV 
    with open(file_to_read, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip headers
        next(csvReader, None)
        
        for row in csvReader:

            # add to id_emp lisy
            id_emp.append(row[0])
            #split name and add to first and last name list
            split_name = row[1].split(" ")
            nm_first.append(split_name[0])
            nm_last.append(split_name[1])
            # read date, format and append to dob list
            dob.append(datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%d/%Y"))
            # parse ,encrypt ssn and append to ssn list
            ssn.append(encrpty_ssn(row[3]))
            # look up state abreviation and append to ssn list
            state.append(get_state_abbrev(row[4]))
                                  

# Zip lists together for all the files read
cleanCSV = zip(id_emp, nm_first,nm_last,dob, ssn,state)


with open(newemployeeCSV, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

        # Write the zipped lists to a csv
        csvWriter.writerows(cleanCSV)
