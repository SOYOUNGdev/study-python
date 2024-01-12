# # 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
# fruits = ['aPPle', 'BananA', 'meLON']
# print(list(map(lambda fruit: fruit.lower(), fruits)))

# # 입력받은 한글을 정수로 변경
# # 입력 예: 삼오일구
# # 출력 예: 3519
# hangul = "공일이삼사오육칠팔구"
# data = "삼오일구"
#
# map을 이용하여 data를 하나씩 받아온다.(삼 -> 오 -> 일-> 구)
# 받아온 데이터 하나씩 hangul의 문자와 일치하는 문자가 들어있는 인덱스값을 s에 저장
# list를 이용해서 [3, 5, 1, 9]
# 각각이 정수이므로 join이용하여 하나의 문자열로 만든다.
# print(int("".join(list(map(lambda s: str(hangul.index(s)), data)))))

# # 입력받은 정수를 한글로 변경
# # 입력 예: 3519
# # 출력 예: 삼오일구
# hangul = "공일이삼사오육칠팔구"
# data = 3519

# hangul의 3,5,1,9번째 인덱스에 있는 값 저장
# (현재 3,5,1,9은 문자이므로 정수로 변환 필요!)
# 변환하는 법 2가지(1. int(), 2.아스키코드)
# # print("".join(list(map(lambda s: hangul[int(s)], str(data)))))
# print("".join(list(map(lambda s: hangul[ord(s) - 48], str(data)))))

# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
print(list(map(lambda url: url.split("/")[0], urls)))

# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
# print(list(filter(lambda url: url.split("/")[0] != 'user', urls)))
print(list(filter(lambda url: url.split("/")[0] != 'user', list(map(lambda url: url.split("/")[0], urls)))))