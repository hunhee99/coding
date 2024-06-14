x = int(input())  # Get input from the user and convert it to an integer
dp = [0] * (x+1)  # Create a list of size x+1 filled with zeros to store the minimum number of operations for each number
for i in range(2, x+1):  # Iterate from 2 to x (inclusive)
    dp[i] = dp[i-1] + 1  # Set the minimum number of operations for i to the minimum number of operations for i-1 plus 1
    if i % 2 == 0:  # If i is divisible by 2
        dp[i] = min(dp[i], dp[i//2] + 1)  # Update the minimum number of operations for i if necessary
    if i % 3 == 0:  # If i is divisible by 3
        dp[i] = min(dp[i], dp[i//3] + 1)  # Update the minimum number of operations for i if necessary
print(dp[x])  # Print the minimum number of operations for x
