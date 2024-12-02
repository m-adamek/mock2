# (p5.py) Define a function f(first_letter,last_letter) that, 
# for the data.txt file, returns the number of words that 
# start with the first_letter and end with the last_letter.
# 
# Example:
# f("w","d")  compare your result with other students

import re

def f(first_letter, last_letter):
    with open('data.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    pattern = r'\b' + re.escape(first_letter) + r'\w*' + re.escape(last_letter) + r'\b'
    matching_words = re.findall(pattern, text, flags=re.IGNORECASE)

    return len(matching_words)

print(f("w","d"))