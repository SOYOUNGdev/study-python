# def set_key(key):
#     formatting = ''
#
#     # 클로저
#     def set_value(value):
#         # set_value의 지역변수가 아닌 외부함수 set_key의 formatting 변수임을 알리기 위한 키워드. nonlocal
#         nonlocal formatting
#         formatting = f'{key}: {value}'
#         return formatting
#
#     return set_value
#
# set_name = set_key('이름')    # set_value
# formatting_name = set_name("한동석")             # set_value("한동석")
# print(formatting_name)
#
# # 기초 실습
# # '나이: 00살'
# set_age = set_key('나이')    # set_value
# formatting_age = set_age("20살")             # set_value("20살")
# print(f'{formatting_name}\n{formatting_age}')


# 심화 실습
# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.

# # 방법1(강사님 코드)
# def set_topic(**kwargs):
#     result = 0
#     if 'name' in kwargs:
#         def set_format(sep=', '):
#             formatting = f'name{sep}{kwargs.get("name")}'
#             return formatting
#         result = set_format
#     else:
#         def set_format(sep=', '):
#             formatting = f'{kwargs.get("topic")}{sep}{kwargs.get("point")}'
#             return formatting
#         result = set_format
#
#     # return set_format
#     return result
#
#
# print(set_topic(name='한동석')(': '))
# print(set_topic(topic='지구 온난화', point='오존층 파괴를 막기 위해 인간이 해야할 일')("\n"))


#
# # 방법2(내 코드)
# def set_topic(**kwargs):
#
#     if 'name' in kwargs:
#         name = kwargs['name']
#
#         def set_name(sep=', '):
#             formatting = f'name{sep}{name}'
#             return formatting
#
#         return set_name
#
#     else:
#         topic_and_point = kwargs.get('topic_and_point')
#
#         def set_topic_and_point(sep=', '):
#             topic = kwargs['topic']
#             point = kwargs['point']
#             formatting = f'{topic}{sep}{point}'
#             return formatting
#
#         return set_topic_and_point
#
#
# print(set_topic(name='이름')(': '))
# print(set_topic(topic='주제', point='요약')('\n'))


# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

# 상품 추가, 수정, 정보조회 함수가 들어있는 함수 선언
# set_product 함수는 packing된 상태의 변수를 전달받는다.
# 이 매개변수에는 여러개의 상품정보들이 들어있다.
def set_product(*args):
    # 상품이 추가될 때 마다 1부터 순서대로 번호를 부여하기 위해 number 변수 선언한다.
    number = 0
    # args에는 products(아래에서 미리 작성해놓은 상품정보들)의 주소값이 전달되어있는 상태이다.
    # 이 args들을 하나씩 받아와 product에 저장.
    # 결론적으로, product를 수정하면 products에 직접 접근한 것이므로 products 원본 값이 바뀐다.
    # 전달받은 상품정보의 리스트가 끝날 때까지 상품 하나씩 받아와서
    for product in args:
        # 번호를 1 증가시키고(현재 number가 0이였기 때문)
        number += 1
        # 해당 상품의 number라는 key값에 증가된 번호를 부여한다.
        product['number'] = number

    # 상품 추가
    # 추가할 상품 정보를 keyword arguements 값으로 한번에 받아온다.
    def insert(**kwargs):
        # number와 args는 insert 함수 내에서 선언된 변수가 아닌, 외부에서 선언된 변수라는 걸
        # nonlocal 키워드를 이용하여 알려준다.
        nonlocal number, args
        # 상품을 추가하기 전에 먼저 번호를 1 증가시킨다.
        number +=1
        # args의 자료형은 'tuple' 이므로 +로 추가된 상품의 정보들을 원래 상품목록에 추가한다.
        # tuple은 연결할 때, ','를 붙여야 한다는 사실을 잊지말자!
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'),'number': number},

    # 수정
    # 수정할 상품 정보를 keyword arguements 값으로 한번에 받아온다.
    def update(**kwargs):
        # 전달받은 상품정보의 리스트가 끝날 때까지 상품 하나씩 받아와서
        for product in args:
            # 상품의 번호가 매개변수로 받아온 상품의 번호와 일치하면
            if product['number'] == kwargs.get('number'):
                # 해당 상품의 이름과 가격을 매개변수로 받아온 이름과 가격으로 수정해준다.
                product['name'] = kwargs.get('name')
                product['price'] = kwargs.get('price')
                # 수정하고 난 후의 반복은 의미 없으므로 break를 사용하여 반복문을 종료한다.
                break

    # 목록 조회
    # 조회 함수를 사용하면 상품 목록을 리턴해준다.
    def select_all():
        return args

    # 리턴값으로 함수 여러개를 보내기 위해 자료구조로 묶어서 사용
    # 따라서 추가, 수정, 목록 함수를 사용할 시에는 키 값을 함께 전달해야 해당 함수가 호출된다.
    return {'insert': insert, 'update': update, 'select_all': select_all}

# 미리 작성한 상품정보
products = [
    {'name': '마우스', "price": 5000},
    {'name': '키보드', "price": 25000}
]
# products의 주소 전달
# product_service는 set_product의 리턴 값인
# {'insert': insert, 'update': update, 'select_all': select_all} 가 담겨있다.
# 이 자체가 dict이다
product_service = set_product(*products)
print(products)

# 리턴값인 dict의 키값이 insert인 value값
# 즉, insert함수 자체를 의미
# product_service.get('insert')

# insert함수를 사용하기 위하여 매개변수인 상품명과 가격을 각각 dict 형태(k:v)로 전달한다.
product_service.get('insert')(name='모니터', price=80000)
print(product_service.get('select_all')())

# update함수를 사용하기 위하여 매개변수인 상품명과 가격을 각각 dict 형태(k:v)로 전달한다.
product_service.get('update')(name='키보드', price=20000)
print(product_service.get('select_all')())

# product_info = [
#     {'name': '사과', 'price': 1000},
#     {'name': '배', 'price': 2000},
#     {'name': '복숭아', 'price': 5000}
# ]
# print(type(product_info))
#
# def set_product(*args):
#     result = []
#     # print(type(args)) # 튜플
#     # print(type(args[0]))    # dict
#
#     def insert(*args):
#         number = 1
#         products = [product for product in args]
#         # print(type(products))   # list
#         for product in products:
#             product['number'] = number
#             result.append(product)
#             number += 1
#         return result
#     def update(name, *args):
#
#
#     def select_all(*args):
#         pass
#
#     choice = input('추가, 수정, 조회: ')
#     if choice == '추가':
#         return insert(*args)
#     elif choice == '수정':
#         update_message = '수정할 상품명 입력: '
#         name = input(update_message)
#         if name in result:
#             return update(name, *args)
#     elif choice == '조회':
#         return select_all
#
#
#
#
# set_product(*product_info)
