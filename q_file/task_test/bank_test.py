from total_bank import *

# 이 파일이 실행하는 파일이다.
if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 재설정\n" \
           "6. 거래내역 확인\n" \
           "7. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    new_account_message = "새 계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"


    while True:
        bank_choice = int(input(bank_menu))

        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        # 나가기
        if bank_choice == 4:
            break

        while True:
            menu_choice = int(input(menu))

            if menu_choice == 7:
                break


            if menu_choice == 1:
                user_name = input(owner_message)


                while True:
                    user_account = input(account_number_message)
                    result = Bank.check_account_number(bank_choice, user_account)
                    try:
                        CheckNotNone.check_not_none(result)
                        break
                    except CheckNotNone as e:
                        print(e)


                while True:
                    user_phone = input(phone_message)
                    result = Bank.check_account_number(bank_choice, user_phone)
                    try:
                        CheckNotNone.check_not_none(result)
                        break
                    except CheckNotNone as e:
                        print(e)


                while True:
                    user_password = input(password_message)
                    try:
                        int_user_password = int(user_password)
                        try:
                            PasswordLengthCheck.check_length(user_password)
                            break
                        except PasswordLengthCheck as e:
                            print(e)
                    except ValueError:
                        print('숫자만 입력해주세요.')


                user_balance = int(input(money_message))

                user = Bank.open_account(bank_choice, user_name=user_name, user_account=user_account, user_phone=user_phone, user_password=user_password, user_balance=user_balance)

            # 입금
            elif menu_choice == 2:
                user_account = input(account_number_message)
                user = Bank.check_account_number(bank_choice, user_account)
                deposit_money = 0
                error_code = None

                if user is not None:
                    try:
                        result = (user.get('user_password') == input(password_message))
                        WrongPassword.check_password(result)
                        deposit_money = int(input(deposit_message))

                    except WrongPassword as e:
                        print(e)
                        deposit_money = 0
                        error_code = "비밀번호 오류"

                    finally:
                        user['object'].deposit(deposit_money, error_code=error_code)

                else:
                    print(error_message)


            # 출금
            elif menu_choice == 3:
                user_account = input(account_number_message)
                user = Bank.check_account_number(bank_choice, user_account)
                withdraw_money = 0
                error_code = None

                if user is not None:
                    try:
                        result = (user.get('user_password') == input(password_message))
                        WrongPassword.check_password(result)
                        withdraw_money = int(input(withdraw_message))
                        try:
                            balance = (withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['object'].balance())
                            InsufficientBalance.check_balance(balance)
                        except InsufficientBalance as e:
                            print(e)
                            error_code = "잔액 부족"
                            withdraw_money = 0

                        finally:
                            user['object'].withdraw(withdraw_money, error_code=error_code)

                    except WrongPassword as e:
                        print(e)
                        withdraw_money = 0
                        error_code = "비밀번호 오류"
                        user['object'].withdraw(withdraw_money, error_code=error_code)

                else:
                    print(error_message)


            # 잔액 조회
            elif menu_choice == 4:
                user_account = input(account_number_message)
                user = Bank.check_account_number(bank_choice, user_account)

                if user is not None:
                    print(user)
                    if user.get('user_password') == input(password_message):
                        print(user['object'])
                        print(f"현재 잔액: {user['object'].balance()}")
                        continue
                else:
                    print(error_message)

            # 계좌 번호 재설정
            elif menu_choice == 5:
                user_phone = input(phone_message)
                user = Bank.check_phone(bank_choice, user_phone)
                if user is not None:
                    while True:
                        if user.get('user_password') == input(password_message):
                            while True:
                                new_account = input(new_account_message)
                                if Bank.check_account_number(bank_choice, new_account) is None:
                                    break
                            user['object']['user_account'] = new_account
                            break
                else:
                    print(error_message)

            # 거래내역 보기
            # 자신의 계좌번호와 비밀번호 입력 후, 일치하면 확인가능
            elif menu_choice == 6:
                user_account = input(account_number_message)
                user = Bank.check_account_number(bank_choice, user_account)
                error_code = None

                if user is not None:
                    try:
                        result = (user.get('user_password') == input(password_message))
                        WrongPassword.check_password(result)
                        with open('log.txt', 'r', encoding='utf-8') as file:
                            line = None
                            while line != '':
                                line = file.readline()
                                if user['user_account'] in line:
                                    print(line, end='')

                    except WrongPassword as e:
                        print(e)
                        error_code = "비밀번호 오류"

                else:
                    print(error_message)

            else:
                print(error_message)
