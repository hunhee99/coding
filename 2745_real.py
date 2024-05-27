N, B = map(str, input().split())
N = N[::-1]
B = int(B)

number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

for i in range(len(N)):
    sum = number.index(N[i]) * (B**i)
    result += sum

print(result)