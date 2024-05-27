import sys
input = sys.stdin.readline



n = int(input())    
arr = []
for i in range(n):
    c = input()
    if c[0] == "1":
        arr.append(int(c[2:]))
    elif c[0] == "2":
        if len(arr) != 0:
            t = arr.pop()
            print(t)
        else:
            print(-1)
    elif c[0] == "3":
        print(len(arr))
    elif c[0] == "4":
            if len(arr) != 0:
                print(0)
            else:
                print(1)
    elif c[0] == "5":
            if len(arr) != 0:
                print(arr[-1])
            else:
                print(-1)