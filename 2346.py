from collections import deque

n = int(input())
data = list(enumerate(map(int, input().split()), start = 1))
idx = 0

while data:
    ret = data.pop(idx)
    print(ret[0], end = " ")
    if ret[1] < 0 and data: # 음수면 왼쪽으로 이동
        idx = (idx + ret[1]) % len(data) 
    elif ret[1] > 0 and data: # 양수면 오른쪽으로 이동
        idx = (idx + (ret[1] - 1)) % len(data)