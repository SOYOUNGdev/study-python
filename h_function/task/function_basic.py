# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# ((comprehension을 사용한다.))

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2
#
# 출력 예시1
# [1000, 2000]
#
# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100
#
# 출력 예시2
# [700, 2800, 3500]

# # 방법1 (강사님 코드)
# def use_coupon(*pay, **kwargs):
#     '''
#     :param pay: 주문 금액들
#     :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
#     :return: 할인율이 적용된 주문 금액들
#     '''
#     if 'coupon' in kwargs:
#         return [
#             int((1 - kwargs.get('coupon') * 0.01) * pay[i])
#             for i in
#             range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
#         ]
#     return None
#
# result = use_coupon(1000, 2000, 1000, coupon=50, count=2)
#
# if result:
#     print(result)
# else:
#     print('쿠폰이 없습니다')

# comprehension 사용
# *args에는 주문 금액을, **kwargs에는 '할인율'과 '쿠폰 개수'를 각각 key='value'값으로 전달받는다.
def order(*args, **kwargs):
    '''
    할인율이 적용된 주문 금액 출력
    :param args: 주문 금액들
    :param kwargs: 할인율과 쿠폰 개수
    '''
    # 쿠폰이 적용된 가격만을 저장할 리스트를 만든다.
    discount_prices = []
    # 쿠폰이 부족하여 적용이 안된 가격까지도 저장할 리스트
    discount_or_not_prices = []
    # 할인율이 백분율로(문자열) 되어있기 때문에 %를 없애고 정수로 형변환 해준다.
    discount = int(kwargs.get('coupon').replace("%",""))
    # print(type(discount))     # 할인율이 정수로 잘 변환 됐는지 확인
    # 쿠폰의 개수도 정수로 형변환 해준다.
    cnt = int(kwargs.get('count'))

    # print(type(args))     # <class 'tuple'>
    # 주문 금액을 하나씩 받아와 i에 저장한다.
    # 이 때, 해당 인덱스 번호가 쿠폰의 개수보다 작으면
    # 할인 쿠폰이 적용된 금액(정수로 형변환)으로 discount_or_not_prices 저장되고
    # 해당 인덱스 번호가 쿠폰의 개수보다 크다면
    # 적용할 쿠폰이 없다는 뜻이므로 그냥 주문금액이 저장된다.
    discount_or_not_prices = [
        int(args[i] * ((100 - discount) / 100)) if cnt > i else args[i]
        for i in range(len(args))
    ]
    # discount_prices에는 쿠폰 적용된 금액만 저장하면 되기 때문에,
    # 해당 인덱스 번호가 쿠폰의 개수보다 작으면 할인 금액을 저장하게 된다.
    discount_prices = [
        int(args[i] * ((100 - discount) / 100))
        for i in
        range(cnt if cnt <= len(args) else len(args))
    ]

    # 주문금액이 저장되어있는 리스트를 리턴한다.
    return discount_or_not_prices, discount_prices

pays = [2000, 4000, 2000]
results = order(*pays, coupon='50', count='2')
# print(type(results))      # <class 'tuple'>
print(f'모든 주문 금액은 {results[0]} 이고, 쿠폰이 적용된 주문 금액은 {results[1]} 입니다')
# help(order)

# def order(*args, **kwargs):
    # 컴프리헨션 없이 풀이
    # count = 0
    # discount_prices = []
    # discount = int(kwargs.get('coupon').replace("%", ""))
    # cnt = int(kwargs.get('count'))
    # for i in args:
    #     if cnt != 0:
    #         discount_prices.append(i*((100-discount)/100))
    #         cnt -= 1
    #     else:
    #         discount_prices.append(i)
    # return [int(price) for price in discount_prices]
    # # print(discount_price)
    #
    # # print(f'{kwargs["coupon"]}, {kwargs["count"]}')

# results = order(10000, 20000, 30000, 50000, coupon='30%', count='2')
# print(results)

