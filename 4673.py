def Kaprekar(x):
    arr = []
    while x <= 10000:
        y = str(x)
        for i in y:
            i = int(i)
            x += i  
        if x > 10000:
                break             
        arr.append(x)    
    return set(arr)

set_1 = set()
for i in range(1,10001):
   set_1 = (set_1 | Kaprekar(i))
result = set([i for i in range(1, 10001)])
 
list_1 = (result - set_1)
list_1 = sorted(list_1)

for i in list_1:
    print(i)