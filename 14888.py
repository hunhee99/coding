def calculate_max_min(numbers, operators_count):
    ops = ['+', '-', '*', '/']
    max_result = float('-inf')
    min_result = float('inf')

    def backtrack(index, current_value):
        nonlocal max_result, min_result
        if index == len(numbers) - 1:
            max_result = max(max_result, current_value)
            min_result = min(min_result, current_value)
            return
        next_number = numbers[index + 1]
        for i in range(4):
            if operators_count[i] > 0:
                operators_count[i] -= 1
                if ops[i] == '+':
                    backtrack(index + 1, current_value + next_number)
                elif ops[i] == '-':
                    backtrack(index + 1, current_value - next_number)
                elif ops[i] == '*':
                    backtrack(index + 1, current_value * next_number)
                elif ops[i] == '/':
                    if current_value < 0:
                        backtrack(index + 1, -(-current_value // next_number))
                    else:
                        backtrack(index + 1, current_value // next_number)
                operators_count[i] += 1

    backtrack(0, numbers[0])
    return max_result, min_result

# 입력 받는 부분
n = int(input())
numbers = list(map(int, input().split()))
operators_count = list(map(int, input().split()))

# 함수 실행 및 결과 출력
max_res, min_res = calculate_max_min(numbers, operators_count)
print(max_res)
print(min_res)
