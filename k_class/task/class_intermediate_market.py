# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수
class Product:
    # 상품명, 가격
    # 기본 생성자. 매개변수로 이름과 가격을 받아온 뒤,
    # 할당된 매모리에 저장한다.
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 해당 상품의 정보(상품명, 가격)를 출력한다.
    def print_info(self):
        print(self.name, self.price)

# 손님
# 이름, 나이, 할인율, 잔액
class Customer:
    # 기본 생성자. 이름, 나이, 할인율, 잔액을 매개변수로 받아온다.
    # 할인율과 잔액은 default 값(0)을 설정해준다.
    def __init__(self, name, age, discount=0, money=0):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
class Market:
    # 기본 생성자. 매개변수로 상품과 재고를 받는다.
    # 이때 상품은 Product 객체이다.
    def __init__(self, product: Product, stock: int):
        self.product = product
        self.stock = stock

    # 판매함수
    # 매개변수로 손님을 받는다.
    # 이때, 손님은 해당 손님의 정보가 들어있는 Customer 객체이다.
    def sell(self, customer: Customer):
        # 전달받은 손님으로 접근해서(즉, 객체로 접근해서 해당 필드사용)
        # 해당 손님의 할인율을 계산한다.
        # 상품의 가격은 Market.상품.가격으로(객체) 접근하여 가져온다.
        # 손님의 잔액에서 계산된 상품 가격을 빼준다.
        customer.money -= self.product.price * (1 - customer.discount * 0.01)
        # 상품의 재고도 -1 해준다.
        self.stock -= 1

product = Product('사과', 3000)
customer = Customer('손님1', 20, 30, money=10000)
market = Market(product, 40)
market.sell(customer)
print(market.stock)
print(customer.money)


# # 상품
# # 상품명, 가격
# # 상품의 정보를 print()로 출력하는 함수
# # 상품의 정보
# class Goods:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def print_goods_info(self):
#         print('상품명 : ' + self.name + '가격 : ' + self.price)
#
# # 손님
# # 이름, 나이, 할인율, 잔액
# class Customers:
#     def __init__(self, name, age, discount_rate, change):
#         self.name = name
#         self.age = age
#         self.discount_rate = discount_rate
#         self.change = change
#
#
# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
# # 손님이 온다. 상품을 선택한다. 가격은 상품의 객체에 접근하여 파악한다. 할인율은 손님의 객체에..
# class Market:
#
#     def __init__(self, *goods_info, stock=10):
#         for goods in goods_info:
#             self.goods = goods
#             self.goods.stock = stock
#
#     def sale(self, customer, goods):
#         sale_price = goods.price * (1-customer.discount_rate/100)
#         customer.change -= sale_price
#         goods.stock -= 1
#         return sale_price
#
#
#
#
# goods1 = Goods('상품1', 1000)
# goods2 = Goods('상품2', 2000)
# goods3 = Goods('상품3', 3000)
# goods_info = [goods1, goods2, goods3]
# # goods_info = [Goods('상품1', 1000), Goods('상품2', 2000), Goods('상품3', 3000)]
# # print(type(goods_info))
#
#
# # 손님의 정보
# customer1 = Customers('손님1', 20, 10, 100000)
# customer2 = Customers('손님2', 30, 20, 200000)
# customer3 = Customers('손님3', 18, 15, 80000)
# customers_info = [customer1, customer2, customer3]
#
# market1 = Market(*goods_info)
# # market2 = Market(goods2)
# print(market1.sale(customer1, goods1))
# print(market1.sale(customer1, goods1))
# print(goods1.stock)
# print(market1.sale(customer2, goods2))
# print(goods2.stock)
# print(market1.sale(customer1, goods2))
# print(goods2.stock)