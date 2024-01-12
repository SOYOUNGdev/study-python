from kakao_bank import KaKao
from kookmin_bank import KookMin
from shinhan_bank import ShinHan

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
