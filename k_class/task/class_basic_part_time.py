# PartTimer
#
# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수
#
# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)
#
# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

# 직원 클래스 선언
class PartTimer:
    # 시간 당 급여와 전체 직원 수는 모든 직원이 동일하게 공유하는 것이기 때문에 static 변수로 선언
    # 정적 변수는 PartTimer 클래스 자체로 접근한다. 생성자 호출하지 않아도 메모리가 할당되기 때문이다.
    pay_of_hour = 10000
    total_of_part_timers = 0

    # 직원 한명씩 객체화 될때마다 호출되는 생성자.
    # 각자의 주소값이 부여된다.
    # 닉네임과 지역은 직원마다 다르기 때문에 매개변수로 받는다.
    def __init__(self, nickname, area='청담동'):
        self.nickname = nickname
        self.area = area
        # 급여는 생성자의 매개변수를 통한 초기화가 불가능하게끔 생성자 안에서 초기화한다.
        self.total_price = 0
        # 직원 한 명씩 추가될 때마다, 전체 직원 수 +1
        PartTimer.total_of_part_timers += 1

    # 급여를 계산하는 메소드
    # 해당 직원이 일한 시간과, 상여금을 매개변수로 받는다.
    # 상여금이 없는 경우, 초기값은 0원으로 설정한다.
    def calculate_money(self, work_hours, bonus=0):
        # 해당 직원의 급여 = 일한시간 * 시간 당 급여 + 상여금
        # 여기서 시간 당 급여는 모든 직원이 동일하기 때문에 static 변수로 선언해두었다.
        # 따라서, 접근할 때 객체로 접근하지 않고, 클래스 자체로 접근한다.
        self.total_price += (work_hours * PartTimer.pay_of_hour) + bonus

        # 계산된 급여를 리턴한다.
        return self.total_price

# 닉네임 = '라이언'인 직원을 객체화한다.
# 객체명 = ryan
ryan = PartTimer("라이언")
# 객체로 접근하여 급여를 계산하는 메소드를 호출한다.
# 라이언이 일한 시간은 30시간, 상여금은 600000원 이다.
print(ryan.calculate_money(30, 600000))
# 결과 : 90만원

# 닉네임 = '네오'인 직원을 객체화한다.
# 객체명 = neo
neo = PartTimer("네오", '역삼동')
# 네오라는 직원의 객체로 접근하여 급여를 계산하는 메소드를 호출한다.
# 네오가 일한 시간은 20시간, 상여금은 없다.
print(neo.calculate_money(20))
# 결과 : 20만원

# 전체 직원 수를 확인하기 위해
# 직원 클래스로 접근하여 total_of_part_timers변수를 출력한다.
print(PartTimer.total_of_part_timers)
# 결과 : 2