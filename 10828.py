import sys

t = int(sys.stdin.readline())
stack = [None] * t
top = -1

for _ in range(t):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        top += 1
        stack[top] = cmd[1]
    elif cmd[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif cmd[0] == 'size':
        print(top + 1)
    elif cmd[0] == 'empty':
        print(1 if top == -1 else 0)
    elif cmd[0] == 'top':
        print(-1 if top == -1 else stack[top])
    else:
        print('Invalid command')