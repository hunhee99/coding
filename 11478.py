S = input()
a = []
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        a.append(S[i : j])

print(len(set(a)))