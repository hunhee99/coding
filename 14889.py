from itertools import combinations as com
from itertools import permutations as per
def score(x, list_1):
    arr = list(per(x, 2))
    result = 0
    for i in arr:
        result += list_1[i[0]][i[1]]
    return result


n = int(input())
arr = []
result_list = []


for i in range(n):
    arr_append = list(map(int, input().split()))
    arr.append(arr_append)
    
all_team_list_1 = [i for i in range(n)]
all_team_list_2 = list(com(all_team_list_1, n // 2))
start_team = all_team_list_2[: len(all_team_list_2) // 2]
link_team = all_team_list_2[-1 : len(all_team_list_2) // 2 - 1 : -1]
start_score = []
link_score = []
for i in start_team:
    start_score.append(score(i, arr))
for i in link_team:
    link_score.append(score(i, arr))

for i in range(len(start_team)):
    result_list.append(abs(start_score[i] - link_score[i]))
print(min(result_list))
    