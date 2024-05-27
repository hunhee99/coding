def append_star(Len):
    if Len == 1:
        return ["*"]
    
    Stars = append_star(Len // 3)
    L = []
    
    for S in Stars:
        L.append(S * 3)
    for S in Stars:
        L.append(S + " " * (Len // 3) + S)
    for S in Stars:
        L.append(S * 3)
    return L

n = int(input())
print("\n".join(append_star(n)))