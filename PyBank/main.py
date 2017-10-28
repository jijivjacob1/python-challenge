# import glob
# for file in glob.glob(".csv"):
#     print(file)

# from pathlib import Path
# p = Path(".")
# list(p.glob("*.py"))

import os
import csv
files_to_process = []
path_to_read = "./raw_data"
path_to_write = "./output"
for file in os.listdir(path_to_read):
    if file.endswith(".csv"):
        files_to_process.append(file)
# print(files_to_process)




for file in files_to_process:
    financial_data = {}

    file_to_read = os.path.join(path_to_read, file)

    with open(file_to_read, 'r') as csvFile:
        dict_reader = csv.DictReader(csvFile)
        for row in dict_reader:
            # print("{Date}, {Revenue}".format(**row))
            # print(type(row["Revenue"]))
            financial_data[row["Date"]] = int(row["Revenue"])

    total_months = len(list(financial_data.keys()))
    total_revenue = sum(financial_data.values())
    avg_rev_change = int(round(total_revenue / total_months ,0))
    maximum_key = max(financial_data, key=financial_data.get)
    maximum_value = financial_data[maximum_key]
    minimum_key = min(financial_data, key=financial_data.get)
    minimum_value = financial_data[minimum_key]
    print("\n"+"="*50)
    print(f"\nFinancial Analysis for {file}")
    print("\n"+"="*50)
    # print("/n")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${avg_rev_change}")
    print(F"Greatest Increase in Revenue: {maximum_key} (${maximum_value})")
    print(F"Greatest Decrease in Revenue: {minimum_key} (${minimum_value})")

    
    file_to_write = os.path.join(path_to_write, (file.split("."))[0] + ".txt")
    with open(file_to_write, 'w') as filewriter:

        print(f"\nFinancial Analysis for {file}",file=filewriter)
        print("="*50,file=filewriter)
        print(f"Total Months: {total_months}",file=filewriter)
        print(f"Total Revenue: ${total_revenue}",file=filewriter)
        print(f"Average Revenue Change: ${avg_rev_change}",file=filewriter)
        print(F"Greatest Increase in Revenue: {maximum_key} (${maximum_value})",file=filewriter)
        print(F"Greatest Decrease in Revenue: {minimum_key} (${minimum_value})",file=filewriter)

    
    