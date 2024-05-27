import sys
input = sys.stdin.readline
N, M = map(int, input().split())
name_dic = {}

for i in range(N):
    name = input()
    name_dic[name] = i + 1
index_dic = {v : k for k,v in name_dic.items()}

for i in range(M):
    q = input()
    if q in name_dic:
        print(name_dic[q])
    else:
        print(index_dic.get(int(q)), end= "")
