from total_bank import Bank

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