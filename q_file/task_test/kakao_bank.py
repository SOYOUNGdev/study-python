from total_bank import Bank

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