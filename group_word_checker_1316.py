# set과 짭set 만들어서 길이 비교
N = int(input())
arr = []
for i in range(N):
    word = input()
    arr.append(word)
count_list = []
    
for i in arr:
    key_set = set(i)
    key_set = list(key_set) 
    key_list = []
    s = list(i)
    for j in range(len(s)):
        try:
            if s[j] != s[j + 1]:
                key_list.append(s[j])
        except IndexError:
            key_list.append(s[j])
    
    if len(key_set) == len(key_list):
        count_list.append(1)
print(count_list.count(1))
        
        
        
        
        
        