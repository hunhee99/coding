N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in A:
    i -= B
    cnt += 1
    if i <= 0:
        continue
    elif i > C:
        cnt += i // C
        if i % C != 0:
            cnt += 1
    else:
        cnt += 1
print(cnt)


