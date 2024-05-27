x = int(input())

cnt = 1
updown = 0
arr = []

cnt_1 = 1
updown_1 = 1
arr_1 = []

while x > len(arr):   # 분자
    if updown == 0:
        for i in range(cnt, 0, -1):
            arr.append(i)
        cnt += 1
        updown = 1
    else :
        for i in range(1, cnt + 1):
            arr.append(i)
        cnt += 1
        updown = 0

while x > len(arr_1):    #분모
    if updown_1 == 0:
        for i in range(cnt_1, 0, -1):
            arr_1.append(i)
        cnt_1 += 1
        updown_1 = 1
    else :
        for i in range(1, cnt_1 + 1):
            arr_1.append(i)
        cnt_1 += 1
        updown_1 = 0

print(f"{arr[x - 1]}/{arr_1[x - 1]}")
