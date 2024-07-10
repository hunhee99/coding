def hex_to_decimal(hex_num):
    hex_num = list(hex_num)
    hex_num.reverse()
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    decimal = 0
    for i in range(len(hex_num)):
        decimal += hex_digits.index(hex_num[i]) * (16 ** i)
    return decimal

hex_num = input()
decimal_num = hex_to_decimal(hex_num)
print(decimal_num)