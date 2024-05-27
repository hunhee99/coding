n, b = map(int, input().split())
result = []
abc_list = [chr(x) for x in range(65, 91)]
num_list = [x for x in range(10, 36)]

while n // b != 0:
    result.append(n % b)
    n = int(n // b)
result.append(n % b)
result.reverse()

for i in range(len(result)):
    if 10 <= result[i] :
        result[i] = abc_list[num_list.index(result[i])]
        

print("".join(map(str,result)))