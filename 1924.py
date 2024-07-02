a = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
print(a[(sum(b[:x - 1]) + y - 1) % 7])