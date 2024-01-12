# 중복 검사
# 매개변수에는 선택한 은행번호(choice)와 계좌번호와 휴대폰 번호를 key, value값으로 받아온 값이 있다.
# 넘어온 key 값이 'user_account'라면 계좌번호 중복 검사이고,
# 'user_phone'이라면 핸드폰 번호 중복 검사이다.
def check(choice, key, value):
    # 선택한 은행 리스트에서 회원 정보를 한명씩 받아온다.
    for user in Bank.banks[choice-1]:
        # print(type(user))     # <class 'dict'>
        # 매개변수로 받은 번호와 같은 계좌번호 또는 핸드폰 번호가 있다면
        if value == user.get(key):
            # 그 회원을(user) 리턴한다
            return user
    # 없다면 None을 리턴한다.(주소x)
    else:
        return None

# 은행 클래스(부모 클래스)
class Bank:
    # 전체 은행 수
    total_count = 3
    # 은행 2차원 배열로 생성
    # comprehension 이용
    banks = [
        [] for bank in range(total_count)
    ]

    # 기본 생성자
    def __init__(self, **kwargs):
        # 각 회원의 objet 필드에는 필드의 주소값이 담긴다.
        # user가 dict로 담겨있기 때문에 객체를 가져오기 위해서 필요한 코드이다.
        self.object = self
        self.user_name = kwargs['user_name']
        self.user_account = kwargs['user_account']
        self.user_phone = kwargs['user_phone']
        self.user_password = kwargs['user_password']
        self.user_balance = kwargs['user_balance']

    # 계좌 조회(중복없음)
    # Bank라는 클래스 자체로 접근할 수 있도록 static메소드로 선언한다.
    # 즉, self에 접근하는 메소드가 아니다.
    @staticmethod
    def check_account_number(choice, user_account):
        # print('계좌 조회 함수 실행')
        # 계좌번호 중복 검사를 위한 check함수 호출이므로,
        # 사용자가 선택한 은행번호와
        # key값으로는 user_account를,
        # value값으로는 전달받은 계좌번호(즉, 사용자가 입력한 계좌번호)를 넘겨준다.
        result = check(choice, key='user_account', value=user_account)
        # 결과를 리턴한다.(user 또는 None)
        return result

    # 핸드폰 번호 조회(중복없음)
    # Bank라는 클래스 자체로 접근할 수 있도록 static메소드로 선언한다.
    @staticmethod
    def check_phone(choice, user_phone):
        # 핸드폰 번호 중복 검사를 위한 check함수 호출이므로,
        # 사용자가 선택한 은행번호와
        # key값으로는 user_phone을,
        # value값으로는 전달받은 핸드폰 번호(즉, 사용자가 입력한 핸드폰 번호)를 넘겨준다.
        # print('핸드폰 번호 조회 함수 실행')
        # 결과를 리턴한다.
        return check(choice, key='user_phone', value=user_phone)

    # 계좌 신규 계설 시, 이용할 생성자
    # 선택한 은행번호, Bank클래스에 들어갈 여러 회원 정보들을 **kwargs를 이용해 받는다.
    @classmethod
    def open_account(cls, choice, **kwargs):
        # cls.banks[choice - 1].append(user.__dict__)

        # bank = 선택한 은행 번호 - 1 에 해당하는 클래스의 객체를 생성한다.(생성자 호출)
        # 예) 1 -> 0번 인덱스 -> 신한 / 2 -> 1번 인덱스 -> 국민 / 3 -> 2번 인덱스 -> 카카오
        user = [ShinHan, KookMin, KaKao][choice - 1](**kwargs)  # ShinHan(**kwags)
        # 입력받은 회원의 정보를 dictionary 타입으로 리스트에 저장한다.
        # check 함수에서 원하는 key로 회원의 정보를 찾기 위함이다.
        user_info = {'object': user, 'user_name': kwargs['user_name'], 'user_phone': kwargs['user_phone'],
         'user_password': kwargs['user_password'], 'user_account': kwargs['user_account'], 'user_balance': user_balance}
        cls.banks[choice - 1].append(user_info)
        # 개설된 회원 정보를 리턴한다.
        # 선택한 은행 객체로 생성된 사용자가 입력한 정보가 dict 타입으로 담긴 객체
        # print(type(user))   # <class '__main__.ShinHan'> / <class '__main__.KookMin'> / <class '__main__.KaKao'>
        return user

    # 입금
    # 사용자가 입력한 입금액을 매개변수로 받아온다.(money)
    def deposit(self, money: int):
        # 해당 객체의 잔액에 + 해준다.
        self.user_balance += money

    # 출금
    # 사용자가 입력한 출금액을 매개변수로 받아온다.(money)
    def withdraw(self, money: int):
        # 해당 객체의 잔액에 - 해준다.
        self.user_balance -= money

    # 통장 잔고
    def balance(self):
        # 해당 객체의 잔액을 그대로 리턴해준다.
        return self.user_balance

    # 객체를 출력할 때마다 사용되지만, 평상시에 생략되어있던 메소드를 재정의하여,
    # 객체를 출력하는 것만으로도, 원하는 문자열로 출력할 수 있도록 한다.
    def __str__(self):
        return f'{self.user_name}, {self.user_account}, {self.user_phone}, {self.user_password}, {self.user_balance}'

# 신한은행
# 은행을 상속 받는 자식 클래스이다.
# 입금 시, 수수료 50%
class ShinHan(Bank):
    # 입금할 때의 메소드를 재정의한다.(Overriding)
    # 입금액을 매개변수로 받아와서, 반으로 나누고
    # 그 금액을 부모클래스의 입금 함수의 매개변수로 전달해준다.
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)

# 국민은행
# 은행을 상속 받는 자식 클래스이다.
# 출금 시, 수수료 50%
class KookMin(Bank):
    # 출금할 때의 메소드를 재정의한다.(Overriding)
    # 출금액을 매개변수로 받아와서, 1.5배 하고
    # 그 금액을 부모클래스의 출금 함수의 매개변수로 전달해준다.
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(money)

# 카카오 은행
# 은행을 상속 받는 자식 클래스이다.
# 잔액 조회 할때마다, 재산 반토막
class KaKao(Bank):
    # 잔액 조회할 때의 메소드를 재정의한다.(Overriding)
    # 현재 잔액을 반으로 나눈뒤
    # 부모클래스의 잔액조회 함수를 호출한다.
    def balance(self):
        self.user_balance //= 2
        return super().balance()

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