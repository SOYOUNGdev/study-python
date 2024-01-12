from total_bank import Bank
from kakao_bank import KaKao
from kookmin_bank import KookMin
from shinhan_bank import ShinHan

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
           "6. 은행 선택 메뉴로 돌아가기\n"

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
        # 은행 메뉴
        # bank_choice = 사용자가 선택한 은행
        bank_choice = int(input(bank_menu))

        # 메뉴의 번호 이외의 번호를 입력 시 밑으로 내려가지 않게 하기 위함
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        # 나가기
        if bank_choice == 4:
            break

        while True:
            # 서비스 메뉴
            # menu_choice = 사용자가 선택한 서비스
            menu_choice = int(input(menu))

            # 은행 선택 메뉴로 나가기
            if menu_choice == 6:
                break

            # 개설
            if menu_choice == 1:
                # 사용자 이름
                user_name = input(owner_message)

                # 입력받은 계좌번호의 중복검사를 위해 중복 검사 함수를 호출한다.
                # 이 때, check_account_number()는 static 메소드로 선언되어있기 때문에, 클래스(Bank)로 접근한다.
                # 매개변수로는 선택한 은행과 입력한 계좌번호를 전달하며
                # 중복되는 번호가 없다면, 반복문을 빠져나온다.
                while True:
                    user_account = input(account_number_message)
                    # None은 False값이지만, 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.
                    if Bank.check_account_number(bank_choice, user_account) is None:
                        break

                # 입력받은 핸드폰 번호의 중복검사를 위해 중복 검사 함수를 호출한다.
                # 이 때, check_phone()는 static 메소드로 선언되어있기 때문에, 클래스(Bank)로 접근한다.
                # 매개변수로는 선택한 은행과 입력한 핸드폰 번호를 전달하며
                # 중복되는 번호가 없다면, 반복문을 빠져나온다.
                while True:
                    user_phone = input(phone_message)
                    if Bank.check_phone(bank_choice, user_phone) is None:
                        break

                # 입력받은 비밀번호가 4자리라면 반복문을 빠져나온다.
                while True:
                    user_password = input(password_message)
                    if len(user_password) == 4:
                        break

                # 사용자가 입력한 예치금
                user_balance = int(input(money_message))

                # user = Bank 클래스 객체
                # 계좌가 계설된다.
                # 어떤 은행에서 개설했는지를 bank_choice에 담아서 전달한다.
                # open_account()는 회원의 정보를 **kwargs로 받기 때문에 사용자가 입력한 정보를 모두 풀어서 전달해준다.
                user = Bank.open_account(bank_choice, user_name=user_name, user_account=user_account, user_phone=user_phone, user_password=user_password, user_balance=user_balance)

                # 개설된 계좌 정보 출력
                print(user)

            # 입금
            elif menu_choice == 2:
                # 사용자가 입력한 계좌번호가 있는지 확인하기 위해
                # 중복검사 함수인 check_account_number()를 호출한다.
                user_account = input(account_number_message)
                user = Bank.check_account_number(bank_choice, user_account)
                # 결과가 None이 아니라면 해당 계좌를 가진 회원이 있다는 의미이다.
                # None은 False값이지만, 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.
                # user는 회원 정보가 dict 타입으로 저장되어있다.
                if user is not None:
                    # 따라서, 사용자에게 비밀번호를 입력받아
                    # 해당 객체의 비밀번호와 같다면
                    if user.get('user_password') == input(password_message):
                        # 현재 선택된 은행이 신한은행인지 검사한다.
                        if isinstance(user.get('object'), ShinHan):
                            # 신한은행이 아니라면
                            if bank_choice != 1:
                                # 입금을 할 수 없다는 것을 알리는 메세지를 출력한다.
                                print('개설한 은행에서만 입금서비스를 사용하실 수 있습니다.')
                                # 입금액을 입력받는 코드가 실행되지 못하도록 continue를 사용한다.
                                continue
                        # 입금액을 입력받고
                        deposit_money = int(input(deposit_message))
                        # 해당 객체로 접근하여 입금함수를 호출한다.
                        # 이 때, user['object']에는 객체(self)가 저장되어있기 때문에 함수를 호출할 수 있다.
                        user['object'].deposit(deposit_money)
                        # 에러 메세지 출력을 막기위해 continue 사용
                        continue
                else:
                    print(error_message)


            # 출금
            elif menu_choice == 3:
                # 사용자가 입력한 계좌번호가 있는지 확인하기 위해
                # 중복검사 함수인 check_account_number()를 호출한다.
                user_account = input(account_number_message)
                user = Bank.check_account_number(bank_choice, user_account)
                # 결과가 None이 아니라면 해당 계좌가 있다는 의미이다.
                # user는 회원 정보가 dict 타입으로 저장되어있다.
                if user is not None:
                    # 따라서, 사용자에게 비밀번호를 입력받아
                    # 해당 객체의 비밀번호와 같다면
                    if user.get('user_password') == input(password_message):
                        # 출금액을 입력받고
                        withdraw_money = int(input(withdraw_message))
                        # 해당 객체의 타입이 국민이라면, 출금액 * 1.5 <= 현재 잔고,(출금수수료 = 50%)
                        # 해당 객체의 타입이 국민이 아니라면, 출금액 <= 현재 잔고 일 경우에만
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            # 해당 객체로 접근하여 출금함수를 호출한다.
                            user['object'].withdraw(withdraw_money)
                        else:
                            print(error_message)
                else:
                    print(error_message)


            # 잔액 조회
            elif menu_choice == 4:
                # 사용자가 입력한 계좌번호가 있는지 확인하기 위해
                # 중복검사 함수인 check_account_number()를 호출한다.
                user_account = input(account_number_message)
                user = Bank.check_account_number(bank_choice, user_account)
                # 결과가 None이 아니라면 해당 계좌가 있다는 의미이다.
                # user는 회원 정보가 dict 타입으로 저장되어있다.
                if user is not None:
                    # 따라서, 사용자에게 비밀번호를 입력받아
                    # 해당 객체의 비밀번호와 같다면
                    if user.get('user_password') == input(password_message):
                        # 해당 객체로 접근하여 잔액조회 메소드를 호출한다.
                        print(f'현재 잔액: {user["object"].balance()}')
                        # 에러 메세지 출력 막기위해 continue 사용
                        continue
                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
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
                            # 새롭게 설정한 계좌번호로 등록한다.
                            # 계좌를 개설할 때 __dict__로 저장했다.
                            # 이 때 __dict__를 수정하는 것 보다, 객체로 직접 접근해서 바꾸는 것이 안전하다.
                            # 결국, __dict__도 self를 받아서 만들어진 객체이므로, 뿌리인 self로 접근하는 것이 좋다.
                            user['object']['user_account'] = new_account
                            # print(user)
                            break
                else:
                    print(error_message)

            else:
                print(error_message)