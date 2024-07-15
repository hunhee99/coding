import sys 
input = sys.stdin.readline


n = int(input())
a = -1 * (n - 1)  # Initialize a with -1 * (n - 1)

for i in range(n):
    a += int(input())  # Add each input to a directly

print(a)
