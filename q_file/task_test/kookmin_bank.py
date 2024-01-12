from total_bank import Bank

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