x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())
x_4, y_4 = None, None


if x_1 == x_2:
    x_4 = x_3
elif x_1 == x_3:
    x_4 = x_2 
else :
    x_4 = x_1 
              
if y_1 == y_2:
    y_4 = y_3
elif y_1 == y_3:
    y_4 = y_2 
else :
    y_4 = y_1 
    
print(f"{x_4} {y_4}")