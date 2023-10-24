# Samuel Barker
# sbarker1@my.athens.edu
# Exam 2 On-Campus, Problem 2

# References: 
# [1] https://www.geeksforgeeks.org/python-convert-list-of-tuples-into-list/#
# [2] https://stackoverflow.com/questions/43421749/given-a-file-return-a-list-of-tuples-representing-the-lines-in-the-file-on-pyth


import csv # To assist in reading .csv files, # [1]
import os

def readCoordinates(filename):
    if not os.path.exists(filename):
        print(f"The file {filename} does not exist.")

        return []

    locationData = []

    # [2]
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',') 

        for row in csv_reader:
            if len(row) >= 2:
                x, y = map(int, row)
                locationData.append((x, y))

    return locationData

# File path can be changed, this is for example purposes. 
file_path = r'C:\Users\erbab\Desktop\e2p2data.csv'
location = readCoordinates(file_path)

# Verify whether or not file has been found and loaded. 
if location:
    print("Data file is loaded successfully.")
    print(location)
else:
    print("No data has been loaded.")

