x = int(input())
y = int(input())
z = int(input())

set_1 = set([x, y, z])

if x + y + z != 180:
    print("Error")
elif len(set_1) == 1:
    print("Equilateral")
elif len(set_1) == 2:
    print("Isosceles")
else:
    print("Scalene")