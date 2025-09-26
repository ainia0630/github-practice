# bank_app.py

accounts = {}  # { 계좌ID(int): {"name": str, "balance": int} }

MENU = """-----Menu-----
1. 계좌개설
2. 입금
3. 출금
4. 계좌번호 전체 출력
5. 프로그램 종료
선택(1~5까지의 숫자만 입력) : """

def create_account():
    print("\n[계좌개설]")
    # 계좌ID
    while True:
        try:
            acc_id = int(input("계좌ID:(숫자로 입력) "))
            if acc_id in accounts:
                print("❌ 이미 존재하는 계좌ID입니다. 다른 번호를 입력하세요.")
                continue
            break
        except ValueError:
            print("❌ 숫자만 입력 가능합니다.")
    # 이름
    name = input("이름: ").strip()
    # 입금액
    while True:
        try:
            init_deposit = int(input("입금액: "))
            if init_deposit < 0:
                print("❌ 음수는 불가합니다.")
                continue
            break
        except ValueError:
            print("❌ 숫자만 입력 가능합니다.")
    accounts[acc_id] = {"name": name, "balance": init_deposit}

def deposit():
    try:
        acc_id = int(input("\n[입금]\n계좌ID: "))
        if acc_id not in accounts:
            print("❌ 존재하지 않는 계좌입니다.")
            return
        amount = int(input("입금액: "))
        if amount <= 0:
            print("❌ 0 이하 금액 불가.")
            return
        accounts[acc_id]["balance"] += amount
        print(f"✅ 입금 완료. 현재 잔액: {accounts[acc_id]['balance']}")
    except ValueError:
        print("❌ 숫자만 입력 가능합니다.")

def withdraw():
    try:
        acc_id = int(input("\n[출금]\n계좌ID: "))
        if acc_id not in accounts:
            print("❌ 존재하지 않는 계좌입니다.")
            return
        amount = int(input("출금액: "))
        if amount <= 0:
            print("❌ 0 이하 금액 불가.")
            return
        if accounts[acc_id]["balance"] < amount:
            print("❌ 잔액이 부족합니다.")
            return
        accounts[acc_id]["balance"] -= amount
        print(f"✅ 출금 완료. 현재 잔액: {accounts[acc_id]['balance']}")
    except ValueError:
        print("❌ 숫자만 입력 가능합니다.")

def print_all():
    if not accounts:
        print("\n등록된 계좌가 없습니다.")
        return
    print()
    for acc_id, info in accounts.items():
        print(f"계좌ID: {acc_id}")
        print(f"이름: {info['name']}")
        print(f"잔액: {info['balance']}\n")

def main():
    while True:
        try:
            choice = int(input(MENU))
        except ValueError:
            print("❌ 숫자만 입력 가능합니다.\n")
            continue

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print_all()
        elif choice == 5:
            break
        else:
            print("❌ 1~5 사이 숫자만 선택하세요.\n")

if __name__ == "__main__":
    main()
