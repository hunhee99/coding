n = int(input())
ListWhoMeet = ["ChongChong"]
for i in range(n):
    h1, h2 = map(str,input().split())
    if h1 in ListWhoMeet:
        ListWhoMeet.append(h2)
    elif h2 in ListWhoMeet:
        ListWhoMeet.append(h1)
print(len(set(ListWhoMeet)))