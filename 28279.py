from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque([])
for i in range(n):
    com = input().split()
    
    if com[0] == "1":
        q.appendleft(int(com[1]))
    elif com[0] == "2":
        q.append(int(com[1]))
    elif com[0] == "3":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif com[0] == "4":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif com[0] == "5":
        print(len(q))
    elif com[0] == "6":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == "7":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif com[0] == "8":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])