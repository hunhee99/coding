n = int(input())


stack_1 = list(map(int, input().split()))

stack_2 = []
k = 1

while stack_1:
    if k == stack_1[0]:
        k += 1
        stack_1.pop(0)
    else:
        stack_2.append(stack_1.pop(0))    
    while stack_2:
        if stack_2[-1] == k:
            stack_2.pop()    
            k += 1        
        else:
            break

if len(stack_2) == 0:
    print("Nice") 
else:
    print("Sad")   