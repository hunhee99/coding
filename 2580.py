test = []
blank = []
for i in range(9):
    test.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if test[i][j] == 0:
            blank.append((i,j))

def row(x, a):
    for i in range(9):
        if a == test[x][i]:
            return False
    return True
def col(y, a):
    for i in range(9):
        if a == test[i][y]:
            return False
    return True

def rect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == test[nx + i][ny + j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*test[i])
        exit(0)
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        
        if row(x,i) and col(y, i) and rect(x, y, i):
            test[x][y] = i
            dfs(idx + 1)
            test[x][y] = 0
            
dfs(0)