while True:
    x, y, z = map(int, input().split())
    list_1 = [x, y, z]
    set_1 = set(list_1)
    if sum(list_1) == 0:
        break
    if (sum(list_1) - max(list_1)) <= max(list_1):
        print("Invalid")
    elif len(set_1) == 1:
        print("Equilateral")
    elif len(set_1) == 2:
        print("Isosceles")
    elif len(set_1) == 3:
        print("Scalene")
    
    