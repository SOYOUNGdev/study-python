# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).

# 회원 클래스
class User:
    # 회원 번호: 전역변수 -> 0으로 초기화 되어있는 상태
    # private: 자신의 클래스에서만 접근 가능
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
    __number = 0

    # 기본 생성자.
    # 매개변수로 해당 객체가 생성된 주소값(self)과
    # 아이디, 비밀번호, 이름을 전달받는다.
    def __init__(self, id, password, name):
        # User클래스로 접근하여 회원번호를 1증가 시킨다.
        User.__number += 1
        self.id = id
        self.password = password
        self.name = name

    # 객체가 아닌 클래스로 접근하기 위해 회원번호를 가져오는 함수는 static 메소드로 선언한다.
    @staticmethod
    def get_number(self):
        # 해당 회원의 번호를 리턴한다.
        return User.__number

    # 관리자로 가입할 경우, 기본 생성자가 아닌 sign_in_admin()을 사용한다.
    # 매개변수는 여러개의 key,value로 이루어진 정보를 **kwargs로 packing하여 전달 받는다.
    @classmethod
    def sign_in_admin(cls, **kwargs):
        # 'id'라는 키에 해당하는 value값에 관리자 표기('admin_')을 붙여서 저장한다.
        kwargs['id'] = 'admin_' + kwargs['id']
        # 매개변수로 받았던 정보를 기본 생성자에 전달한다.
        return cls(**kwargs)

user1 = User('abcd1234', '1111', '이름1')
print(user1.id, user1.get_number(user1))
admin1 = User.sign_in_admin(id='ad1234', password='1234', name='관리자1')
print(admin1.id, admin1.get_number(admin1))

# class User:
#     number = 0
#     def __init__(self, **kwargs):
#         User.number += 1
#         self.id = kwargs['id']
#         self.password = kwargs['password']
#         self.name = kwargs['name']
#
#
#     @classmethod
#     def sign_in_admin(cls, **kwargs):
#         kwargs['id'] = 'admin_' + kwargs['id']
#         return cls(**kwargs)
#
# user1 = User(id='abcd1234', password='1111', name='abcd')
# print(user1.id, user1.number)
# admin1 = User.sign_in_admin(id='ad1234', password='1234', name='admin1')
# print(admin1.id, admin1.number)
