import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nh = []
ns = []

for i in range(n):
    nh.append(input())
for i in range(m):
    ns.append(input())

nh = set(nh)
ns = set(ns)
    
nhns = list(set.intersection(nh, ns))

nhns.sort()
print(len(nhns))
for i in nhns:
    print(i, end = "")