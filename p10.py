# (p10.py) A two-dimensional array contains different integer numbers. 
# Define a function f(array) that returns True if the row and column numbers 
# for the smallest value in the array are equal, and False otherwise.
# 
# Example:
# f([[7,8],[5,3],[9,4]])  True     # 3, row 1, col 1
# f([[7,8,5,3],[9,4,2,6]])  False  # 2, row 1, col 2

def f(array):
    min_value = float('inf')  # Initialize the smallest value as infinity.
    min_row, min_col = -1, -1  # Initialize indices of the smallest value.

    for i, row in enumerate(array):
        for j, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_row, min_col = i, j  # Update indices for the smallest value.

    # Check if row index equals column index.
    return min_row == min_col

# Examples
print(f([[7, 8], [5, 3], [9, 4]]))  # True
print(f([[7, 8, 5, 3], [9, 4, 2, 6]]))  # False






# def f(array):
#     min_value = float('inf')  # Initialize the smallest value as infinity.
#     min_row, min_col = -1, -1  # Initialize indices of the smallest value.

#     # Manual indexing for rows
#     row_index = 0
#     for row in array:
#         col_index = 0
#         for value in row:
#             if value < min_value:
#                 min_value = value
#                 min_row, min_col = row_index, col_index
#             col_index += 1  # Increment column index
#         row_index += 1  # Increment row index

#     # Check if row index equals column index.
#     return min_row == min_col

# # Examples
# print(f([[7, 8], [5, 3], [9, 4]]))  # True
# print(f([[7, 8, 5, 3], [9, 4, 2, 6]]))  # False


# def f(array):
#     # Find the smallest value and its location in the 2D array
#     min_value = min(min(row) for row in array)  # Find the smallest value in the whole array
#     min_row, min_col = None, None

#     # Find the location of the smallest value
#     for i, row in enumerate(array):
#         if min_value in row:
#             min_row = i
#             min_col = row.index(min_value)
#             break  # We found the smallest value, no need to keep searching

#     # Check if the row and column of the smallest value are the same
#     return min_row == min_col