import sys
input = sys.stdin.readline

n = int(input())
dic_log = {}

for i in range(n):
    key_log, value_log = map(str, input().split())
    if value_log == "enter":
        dic_log[key_log] = 1
    else :
        del dic_log[key_log]
name_in_office = sorted(dic_log, reverse=True)

for i in name_in_office:
    print(i)