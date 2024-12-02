# (p7.py) A valid username consists of 4 to 12 characters: lowercase letters, 
# numbers and the underscore character. Define a function f(array) that, 
# for a given array of usernames, returns the number of valid usernames in the array.
# 
# Example:
# f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2

import re

def f(array):
    pattern = r'^[a-z0-9_]{4,12}'

    valid_count = 0

    for username in array:
        if re.fullmatch(pattern, username):
            valid_count +=1

    return valid_count

print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"])) 