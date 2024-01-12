# isinstance : 타입 검사시 사용!!
class A:
    pass

class B(A):
    pass


a = A()
b = B()

print(isinstance(a, A))     # True
print(isinstance(b, B))     # True

# 모든 자식은 '본인 타입'이면서 '부모 타입' 이다.
print(isinstance(b, A))     # True
# 부모는 절대 '자식 타입'이 될 수 없다.
print(isinstance(a, B))     # False