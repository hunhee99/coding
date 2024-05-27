# This code uses a stack to sum up numbers, removing the last added number if a 0 is encountered

k = int(input())  # Read the number of operations
arr = [0]  # Initialize the stack with 0
for i in range(k):
    n = int(input())  # Read the next number
    if n == 0:
        arr.pop()  # Pop the stack if the number is 0
    else:
        arr.append(n)  # Push the number onto the stack
print(sum(arr))  # Print the sum of the stack
