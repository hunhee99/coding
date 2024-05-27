# 좌표평면 위에 사각형이 존재하는 자리에 1을 넣는 형식으로 사각형들의 합집합을 구함 지림


xy_all = [[0 for i in range(101)] for j in range(101)]

n = int(input())


for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            xy_all[j][k] = 1

totall = 0
for item in xy_all:
    totall += sum(item)

print(totall)