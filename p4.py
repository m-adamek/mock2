# The dictionary contains the names of subjects and the grades obtained.
# Define a function f(subjects) that, for the given subjects and their grades,
# returns the name of the subject for which the average grade is the highest.

# Example: 
# f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) à "comp" 

# subjects is a dictionary ??? 

def f(subjects):
    highest_avg = -1
    best_subject = ""

    for subject, grades in subjects.items():
        avg = sum(grades) / len(grades)

        if avg > highest_avg:
            highest_avg = avg
            best_subject = subject

    return best_subject


print(f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}))  # Output: "comp"

