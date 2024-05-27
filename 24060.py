def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = (len(arr) + 1) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merged_arr = []
    
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            merged_arr.append(low_arr[l])
            list_1.append(low_arr[l]) 
            l += 1
        else:
            merged_arr.append(high_arr[h])
            list_1.append(high_arr[h])
            h += 1
    while l < len(low_arr):
        merged_arr.append(low_arr[l])
        list_1.append(low_arr[l])
        l += 1
    while h < len(high_arr):
        merged_arr.append(high_arr[h])
        list_1.append(high_arr[h])
        h += 1
    
    return merged_arr

list_1 = []
N, k = map(int, input().split())
arr = list(map(int, input().split()))
merge_sort(arr)
print(list_1[k - 1] if k <= len(list_1) else -1)