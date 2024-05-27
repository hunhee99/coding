# 벌집
N = int(input())

num_house = 1
cnt = 1

while N > num_house:
    num_house += 6 * cnt
    cnt += 1

print(cnt)