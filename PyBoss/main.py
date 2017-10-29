# import glob
# for file in glob.glob(".csv"):
#     print(file)

# from pathlib import Path
# p = Path(".")
# list(p.glob("*.py"))

import os
import csv
from datetime import datetime

files_to_process = []
path_to_read = "./raw_data"
path_to_output = "./output"
for file in os.listdir(path_to_read):
    if file.endswith(".csv"):
        files_to_process.append(file)
print(files_to_process)

# filepaths = glob.glob("*.csv")
# print(filepaths)



def get_state_abbrev(state_name):
    """Mashes two strings together."""
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

def encrpty_ssn(ssn):
    """Mashes two strings together."""

    ssn_split = ssn.split("-")
    return ('*' * len(ssn_split[0])) + '-' + ('*' * len(ssn_split[1])) + '-' + ssn_split[2]

def split_name(name):
    """Mashes two strings together."""

    names = name.split(" ")
    return names[0],names[1]


  
    

for file in files_to_process:
     # Set empty list variables
    id_emp = []
    nm_first = []
    nm_last = []
    dob = []
    ssn = []
    state = []
    
   # print(files)

    file_to_read = os.path.join(path_to_read, file)
    # Open current wrestling CSV
    with open(file_to_read, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)
        
        for row in csvReader:

            # print(row)
            id_emp.append(row[0])
            nm_first.append(split_name(row[1])[0])
            nm_last.append(split_name(row[1])[1])
            
            dob.append(datetime.strptime(row[2], "%Y-%m-%d").strftime("%d/%m/%Y"))
            ssn.append(encrpty_ssn(row[3]))
            state.append(get_state_abbrev(row[4]))
           
            
            

# Zip lists together
cleanCSV = zip(id_emp, nm_first,nm_last,dob, ssn,state)

for row in cleanCSV:
   print(row)