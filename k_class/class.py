class A:
    # 실제 생성자(메모리에 할당만 해줌. 이 주소값을 init에 전달해준다)
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = super().__new__(cls)
        return obj

    # 실질적으로 데이터를 받아서 처리함. -> 생성자라고 부르기도 함
    def __init__(self, data1, data2, name=''):
        print('__init__')
        print(f'self의 주소값: {self}')
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # def print_name(self, name):
    #     print(name)

    def print_name(self):
        print(self.name)


# 객체화
# 객체 = 생성자(주소값 리턴)
# a = A()
# 필드에 존재하지 않는 변수라면, 변수가 선언된다
# 존재하는 변수라면, 값이 수정된다
# a.data1 = 10
# a.data2 = 20
a = A(10, 20, name='a')
print(f'a의 주소값: {a}')    # 구체화된 a의 주소값
print(a.data1, a.data2)
# a.print_name('a')
a.print_name()

# b = A()
b = A(100, 200, name='b')
print(f'b의 주소값: {b}')
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()
