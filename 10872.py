# This code calculates the factorial of a given number

n = int(input())  # Read an integer input
r = 1  # Initialize result as 1
for i in range(1, n + 1):  # Loop from 1 to n
    r *= i  # Multiply r by i
print(r)  # Print the factorial result
