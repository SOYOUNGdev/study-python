# class Magic:
#     def __init__(self, name):
#         self.name = name
#
#     # # 초기화된 필드를 확인하고자 할 때 사용된다.
#     # def __str__(self):
#     #     return f'name: {self.name}'
#
#     def __str__(self):
#         return f'{self.__repr__()}, __repr__() 사용됨.'
#
# # 객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
# # print(Magic().__repr__())
# # 만약 해당 클래스에서 __str__()을 재정의했다면, __repr__()가 아닌 __str__()이 사용된다.
# # print(Magic().__str__())
# # 따라서, 생략해서 작성하면 __str__()이 붙게된다.
# # print(Magic())
#
# magic = Magic('magic')
# print(magic)
# print(magic.__str__())

# 결과 : name: magic

class Student:
    def __init__(self, number, score):
        self.number = number
        self.score = score

    def __add__(self, other):
        return self.score + other.score

    # def __eq__(self, other):
    #     return self.number == other.number

    def __eq__(self, other):
        if self.__repr__() == other.__repr__():
            print('주소 같음. 들어옴')
            return True

        # 타입 비교
        # isinstance(객체, 타입) : 전달한 객체가 전달한 타입일 경우 True, 아니면 False
        if isinstance(other, Student):
            return self.number == other.number

        return False

std1 = Student(1, 30)
std2 = Student(1, 50)
std3 = std1

# total = std1 + std2
total = std1.__add__(std2)
print(total)
print(std1.__dict__.__getitem__('score'))
print([1, 2, 3].__getitem__(2))

print([1, 2, 3].__contains__(1))    # True
print([1, 2, 3].__contains__(0))    # False

# print(std1 == std2)
# print(std1.__eq__(std2)) # True

# print(std1 == std3)
print(std1.__eq__(std3))    # 결과 : 주소 같음. 들어옴 True
print(std1.__eq__(std2))    # 결과 : True (즉, std2가 Student 객체이므로, std1과 std2의 number가 같은지 검사 -> True 리턴됨)