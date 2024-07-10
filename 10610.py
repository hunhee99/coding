n = input()

# 입력된 숫자에 '0'이 포함되어 있는지 확인
if '0' not in n:
    print(-1)
else:
    # 모든 자릿수의 합이 3의 배수인지 확인
    if sum(map(int, n)) % 3 != 0:
        print(-1)
    else:
        # 가장 큰 숫자를 만들기 위해 내림차순으로 정렬
        max_num = int(''.join(sorted(n, reverse=True)))
        print(max_num)
