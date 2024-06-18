import pandas as pd
from tabulate import tabulate

def produce():
    # 새로운 파일 생성 함수
    print("새로운 파일을 생성합니다.")
    FileName = "Data.csv"
    data = pd.DataFrame({"날짜": [], "적요": [], "수입금액": [], "지출금액": [], "잔액": []})
    data.to_csv(FileName, index=False)
    data.loc[0] = [0, 0, 0, 0, 0]
    data.to_csv("Data.csv", index=False)
    # 완료

def income():
    # 수입 함수
    print("수입 메뉴입니다")
    data = pd.read_csv("Data.csv")
    day_time = input("날짜를 입력하시오 년/월/일 >")
    breiefs = input("적요를 입력하시오 >")
    plus_money = int(input("수입 금액을 입력하시오 >"))
    index_now = len(data)
    balance = data.loc[index_now - 1, "잔액"]
    list_0 = [day_time, breiefs, plus_money, 0, balance + plus_money]
    data.loc[index_now] = list_0
    data.to_csv("Data.csv", index=False)
    # 완료

def expenditure():
    # 지출 함수
    print("지출 메뉴입니다")
    data = pd.read_csv("Data.csv")
    day_time = input("날짜를 입력하시오 년/월/일 >")
    breiefs = input("적요를 입력하시오 >")
    minus_money = int(input("지출 금액을 입력하시오 >"))
    index_now = len(data)
    balance = data.loc[index_now - 1, "잔액"]
    list_0 = [day_time, breiefs, 0, minus_money, balance - minus_money]
    data.loc[index_now] = list_0
    data.to_csv("Data.csv", index=False)
    # 완료

def modify():
    # 수정 함수
    print("수정 메뉴입니다")
    data = pd.read_csv("Data.csv")
    index = int(input("수정할 행 번호를 입력하세요 > "))
    if index < 0 or index >= len(data):
        print("잘못된 행 번호입니다.")
        return
    day_time = input("날짜를 입력하시오 년/월/일 >")
    breiefs = input("적요를 입력하시오 >")
    plus_money = int(input("수입 금액을 입력하시오 >"))
    minus_money = int(input("지출 금액을 입력하시오 >"))
    balance = data.loc[index - 1, "잔액"]
    list_0 = [day_time, breiefs, plus_money, minus_money, balance + plus_money - minus_money]
    data.loc[index] = list_0
    data.to_csv("Data.csv", index=False)
    # 완료

def print_data():
    # 내역 출력 함수
    print("현재까지 내역을 출력합니다")
    data = pd.read_csv("Data.csv")
    print(tabulate(data, headers="keys", tablefmt="fancy_outline"))
    # 완료

# 메인 함수
def main():
    i = 0
    while i == 0:
        command = int(input("원하는 메뉴를 입력하세요. 새로운 파일 생성 또는 초기화 = 0, 수입 금액 작성 = 1, 지출 금액 작성 = 2, 내역 확인 = 3, 수정 = 4, 종료 = 5 > "))
        if command == 0:
            produce()
        elif command == 1:
            income()
        elif command == 2:
            expenditure()
        elif command == 3:
            print_data()
        elif command == 4:
            modify()
        elif command == 5:
            i = 1
            print("프로그램을 종료합니다.")
        else:
            print("잘못된 메뉴 입력입니다")

# 메인 함수 호출
if __name__ == "__main__":
    main()
