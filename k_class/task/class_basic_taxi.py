# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원
#
# 1.
# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 1. 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의
# class Taxi:
#     default_fare = 5800
#     default_distance = 2
#     fare_per_km = 1000
#
#     def __init__(self, money, distance):
#         self.money = money
#         self.distance = distance
#
#     def calculate_fare(self):
#         cost = Taxi.default_fare
#         if self.distance > Taxi.default_distance:
#             cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km
#
#         return cost
#
#     def get_change(self):
#         return self.money - self.calculate_fare()
#
#
# taxi = Taxi(20000, 1)
# print(taxi.calculate_fare(), taxi.get_change())
#
# taxi = Taxi(30000, 10)
# print(taxi.calculate_fare(), taxi.get_change())


# 2.
# 2. 택시 객체 생성 시 택시 수익을 초기화한다.
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달받는다)
# 거리에 따른 잔돈 계산 메소드 정의

# 택시 클래스 선언
# 모든 택시가 동일하게 공유하는 변수(기본요금, 기본거리, km당 추가 요금)는
# static 변수로 선언한다.
# 이들은 객체가 아닌 클래스 자체로 접근할 것이다.
class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    # 생성자
    # 처음 택시 운행 시작 시, 생성자를 통해 수입=0원으로 초기화된다.
    def __init__(self):
        self.income = 0

    # 무조건 요금 계산이 진행된 뒤, 잔돈 계산이 필요하다
    # 따라서, closure를 사용한다.(함수 안에 함수!)
    # 요금 계산을 위해서는, 승객이 낸 돈과 주행 거리가 필요하기 때문에,
    # 매개변수로 받는다.
    def calculate_fare(self, money, distance):
        # 계산 전 기본요금 설정
        # 기본 요금은 static변수로 선언했기 때문에 클래스(Taxi)로 접근한다.
        cost = Taxi.default_fare
        # 주행 거리가 기본 거리보다 많다면,
        if distance > Taxi.default_distance:
            # 결제 요금 = 기본 요금 + (주행 거리 - 기본 거리) * km당 추가 요금
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km

        # 수입에 결제 요금을 누적해준다.
        self.income += cost

        # 잔돈 계산 함수
        # 요금이 계산 되어야만 잔돈 계산 함수가 실행된다
        # 따라서, closure!
        def get_change():
            # 잔돈(승객이 낸 요금 - 결제 요금) 리턴한다.
            return money - cost

        # 결제 요금과, 잔돈 함수 사용 리턴
        return cost, get_change()

taxi= Taxi()
print(taxi.calculate_fare(20000, 1))
print(taxi.calculate_fare(30000, 10))
print(taxi.income)









