# (p2.py) An array contains at least 3 integers. 
# All numbers in the array are equal except one. 
# Define a function f(arr) that returns a number 
# in the arr array that is different from the other numbers. 

# Example: 
# f([7,7,7,7,7,5,7,7]) --> 5 

def f(arr):
    counts = {}
    
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count == 1:
            return num
        
print(f([7, 7, 7, 7, 7, 5, 7, 7]))