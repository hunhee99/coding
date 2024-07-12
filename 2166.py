n = int(input())
x_points = []
y_points = []
for i in range(n):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)
x_points.append(x_points[0])
y_points.append(y_points[0])
result = 0
for i in range(n):
    result += x_points[i] * y_points[i+1]
    result -= x_points[i+1] * y_points[i]
print(abs(result) / 2)