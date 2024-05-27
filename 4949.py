# This code checks if the parentheses and brackets in a given string are properly matched
while True:
    word = input()  # Read input string
    stack = []  # Initialize an empty stack
    if word == ".":
        break  # Exit if the input is a period
    for i in word:
        if i == "(" or i == "[":  # If the character is an opening bracket
            stack.append(i)  # Push it onto the stack
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":  # Check for matching parentheses
                stack.pop()  # Pop the stack if matched
            else:
                stack.append(i)
                break
        elif i == "]": 
            if len(stack) != 0 and stack[-1] == "[":  # Check for matching square brackets
                stack.pop()  # Pop the stack if matched
            else:
                stack.append(i)
                break        
    if len(stack) == 0:
        print("yes")  # Print "yes" if all brackets are matched
    else:
        print("no")  # Print "no" if there are unmatched brackets
