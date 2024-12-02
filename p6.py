# (p6.py) Define a function f(years, course, average_grade) that, 
# for the j file, returns the number of students who are at least 
# the given number of years and have a grade average of at least 
# average_grade in the given course name.
# 
# Example:
# f(21, "statistics", 4)  compare your result with other students

import json


def f(years, course, average_grade):
    # Open the file and load the data
    with open('data.json', 'r') as file:
        students = json.load(file)
    
    count = 0  # Initialize the counter for students meeting the criteria

    # Iterate over each student in the list
    for student in students:
        # Check if the student's age meets the criteria
        if student['age'] >= years:
            # Iterate over each course in the student's studies
            for course_info in student['studies']['courses']:
                # Check if the course name matches the given course
                if course_info['name'].lower() == course.lower():
                    # Calculate the average grade of the student's grades for the course
                    avg_grade = sum(course_info['grades']) / len(course_info['grades'])
                    # Check if the average grade is greater than or equal to the required average_grade
                    if avg_grade >= average_grade:
                        count += 1  # Increment count if the conditions are met
    
    return count  # Return the number of students who meet the criteria

# Example usage:
result = f(21, "statistics", 4)
print(result)
