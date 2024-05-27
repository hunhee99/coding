N = int(input())

for i in range(N):
    a = input()
    score_1 = 0
    b = 1
    for j in range(len(a)):
        
        if a[j] == "O":
            score_1 += b
            b += 1
        else :
            b = 1
    print(score_1)