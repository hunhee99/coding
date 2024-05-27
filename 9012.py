n = int(input())

for i in range(n):
    vps = input()
    vps = list(vps)
    while True:
        if len(vps) == 0 or vps[0] == ")":
            break
        elif vps[0] == "(" and ")" in vps:
            vps.remove("(")
            vps.remove(")")
        else :
            break
    if len(vps) == 0:
        print("YES")
    else:
        print("NO")