class Car:
    # 정적 변수(static variable) :
    # 클래스 내에서 (생성자가 아닌) 선언하는 변수 -> 즉, 모든 객체가 공유하는 변수
    # Car.wheel로 접근하면된다.
    # 생성자 호출을 하지 않아도 컴파일러가 자동으로 메모리에 올려준다.
    wheel = 4

    def __init__(self, brand='', color='', price=0):
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_stop(self):
        print(self.brand + '시동 꺼짐')


# mom_car = Car('Benz', 'Black', 15000)
# daddy_car = Car('BMW', 'Blue', 8800)
#
# mom_car.engine_start()
# daddy_car.engine_start()
#
# print(Car.wheel)
#
# Car.wheel = 6
#
# print(mom_car.wheel)

# new 생성자
cars = [Car, Car]
# init 생성자
mom_car = cars[0]()
daddy_car = cars[1]()
print(mom_car, daddy_car, sep='\n')



