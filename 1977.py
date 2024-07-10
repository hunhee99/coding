import math

# 입력 받기
M = int(input())
N = int(input())

perfect_squares = []

# M 이상 N 이하의 범위에서 완전제곱수 찾기
for i in range(math.ceil(math.sqrt(M)), math.floor(math.sqrt(N)) + 1):
    square = i * i
    if M <= square <= N:
        perfect_squares.append(square)

# 완전제곱수가 없으면 -1 출력
if not perfect_squares:
    print(-1)
else:
    # 합과 최소값 계산
    print(sum(perfect_squares))
    print(min(perfect_squares))
