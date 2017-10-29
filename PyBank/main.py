# -*- coding: UTF-8 -*-
"""PyBank Code."""

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
    financial_data = {}

    #set path to read file from
    file_to_read = os.path.join(path_to_read, file)

    #open file and read via dictionary object
    with open(file_to_read, 'r') as csvFile:
        dict_reader = csv.DictReader(csvFile)
        #Loop through dictionary list and set up
        #dictionary with date as key and revenue as value
        sum_of_delta = 0 
        prev_rev = 0
        for key,item in enumerate(dict_reader):
            #set Revenue as int
            financial_data[item["Date"]] = int(item["Revenue"])
            if key > 0:
                sum_of_delta += (int(item["Revenue"]) - prev_rev)
                prev_rev =  int(item["Revenue"])

    # count the keys to get total months
    total_months = len(list(financial_data.keys()))
    # sum values to get total revenue
    total_revenue = sum(financial_data.values())
    # calculate revenue by dividing total revenue and total months
    avg_rev_change = int(round(sum_of_delta / (total_months - 1) ,0))
    # get key for maximun value
    maximum_key = max(financial_data, key=financial_data.get)
    # get value for the maximun key
    maximum_value = financial_data[maximum_key]
    # get key for maximum value
    minimum_key = min(financial_data, key=financial_data.get)
    # get maximum value
    minimum_value = financial_data[minimum_key]

    #print to console
    print("\n"+"="*50)
    print(f"\nFinancial Analysis for {file}")
    print("\n"+"="*50)
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${avg_rev_change}")
    print(F"Greatest Increase in Revenue: {maximum_key} (${maximum_value})")
    print(F"Greatest Decrease in Revenue: {minimum_key} (${minimum_value})")

    # Open file in output directory and print output to file
    file_to_write = os.path.join(path_to_write, (file.split("."))[0] + ".txt")
    with open(file_to_write, 'w') as filewriter:

        print(f"\nFinancial Analysis ",file=filewriter)
        print("="*50,file=filewriter)
        print(f"Total Months: {total_months}",file=filewriter)
        print(f"Total Revenue: ${total_revenue}",file=filewriter)
        print(f"Average Revenue Change: ${avg_rev_change}",file=filewriter)
        print(F"Greatest Increase in Revenue: {maximum_key} (${maximum_value})",file=filewriter)
        print(F"Greatest Decrease in Revenue: {minimum_key} (${minimum_value})",file=filewriter)

    
    