def recursion(s, i, r, n):
    n += 1
    if i >= r:
        return 1, n
    elif s[i] != s[r]:
        return 0, n 
    else:
        return recursion(s, i + 1, r - 1, n)
def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 0)

N = int(input())

for i in range(N):
    A = input()
    print(isPalindrome(A)[0], isPalindrome(A)[1])