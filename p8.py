# (p8.py) Reverse Polish Notation (RPN) is a mathematical notation in which
# operators follow their operands, e.g. 2 3 + 4 *.
# Define a function f(expression) that, for an RPN expression,
# returns the value of that expression.
# The expression contains only non-negative integers and the + and - operators.
# 
# Example:
# f("2 3 +")  5
# f("2 6 + 4 5 - +")  7
# f("11 7 + 15 - 14 +")  17

def f(expression):
    # Split the expression into tokens
    tokens = expression.split()
    # Initialize an empty stack
    stack = []
    
    # Process each token
    for token in tokens:
        if token.isdigit():  # If it's a number, push onto the stack
            stack.append(int(token))
        else:  # Otherwise, it's an operator
            # Pop the last two numbers from the stack
            b = stack.pop()
            a = stack.pop()
            # Perform the operation and push the result back onto the stack
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
    
    # The final result will be the only item left in the stack
    return stack[0]

# Example usage
print(f("2 3 +"))             # Output: 5
print(f("2 6 + 4 5 - +"))     # Output: 7
print(f("11 7 + 15 - 14 +"))  # Output: 17
