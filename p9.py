# (p9.py) The file data.csv contains a list of employees of the company ABC-Data.
# Define a function f(value) that returns the number of employees
# whose salary is greater than or equal to the given value.
# 
# Example:
# f(9200)  compare your result with other students
# f(11640)  compare your result with other students

import csv

def f(value):
    count = 0

    # Open and read the CSV file
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)  # Read as a dictionary for easier access to columns
        
        for row in reader:
        # Compare the 'Salary' field (convert to int for comparison)
            if int(row['salary']) >= value:
                count += 1
    
    return count

print(f(9200))  
print(f(11640)) 