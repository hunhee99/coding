x, y, w, h = map(int, input().split())
arr = [x, y, h - y, w - x]
print(min(arr))