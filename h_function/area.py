# 전역 변수(global variable)
# 지역 밖에 선언된 변수
# 여러 함수에서 공유해야 하는 값이 있을 경우 사용
#
# 지역 변수(local variable)
# 어떤 지역 안에 선언된 변수

# 전역 변수
count = 0
def increase():
    # print(count)
    # 지역 변수
    # count = 0
    global count    # 함수(지역) 내에서 전역변수를 수정하려면  global 키워드를사용한다.(사용은 그냥 가능)
    count += 1

increase()
print(count)