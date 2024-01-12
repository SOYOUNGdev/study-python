# 인간(부모)
# 이름, 나이
#
# 걷기(walk 메소드)
# '두 발로 걷습니다' 출력
#
# 원숭이(자식)
# 이름, 나이, 동물원 이름
#
# 걷기(walk 메소드)
# '두 발로 걷습니다', '네 발로 걷습니다' 출력

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("두 발로 걷습니다.")

class Monkey(Person):
    def __init__(self, name, age, zoo_name):
        super().__init__(name, age)
        self.zoo_name = zoo_name

    def walk(self):
        super().walk()
        print('네 발로 걷습니다.')


monkey = Monkey('몽킹',3, zoo_name='에버랜드')
monkey.walk()