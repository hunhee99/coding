k = int(input())
x = 0
y = 0
x_points = [0]
y_points = [0]
for i in range(6):
    a, b = map(int, input().split())
    if a == 1:
        x += b
        x_points.append(x)
        y_points.append(y)
    elif a == 2:
        x -= b
        x_points.append(x)
        y_points.append(y)
    elif a == 3:
        y -= b
        x_points.append(x)
        y_points.append(y)
    elif a == 4:
        y += b
        x_points.append(x)
        y_points.append(y)

result = 0
for i in range(6):
    result += x_points[i] * y_points[i+1]
    result -= x_points[i+1] * y_points[i]
print(int((abs(result) / 2) * k))