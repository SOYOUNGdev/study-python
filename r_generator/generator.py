import os
import psutil

process_object = psutil.Process(os.getpid())
# rss는 메모리 사용량이 바이트로 리턴된다. 값이 너무 크기때문에 1024로 두번 나누어서 메가바이트로 출력
# (바이트 -> 킬로바이트 -> 메가바이트)
memory_before = process_object.memory_info().rss / 1024 / 1024

data_list = [i ** 2 for i in range(1000)]
# 리스트 전체 리턴
print(data_list)

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'{memory_before} -> {memory_after}')
# 결과 : 13.98828125 -> 14.05078125 (메모리 사용량이 증가함)

##############################################################################

memory_before = process_object.memory_info().rss / 1024 / 1024

data_generator = (i ** 2 for i in range(1000))
# generator 객체로 리턴된다.
# print(data_generator)   # <generator object <genexpr> at 0x00000190300228F0>
# 따라서 값을 가져오기 위해서 next를 사용해야한다.
print(next(data_generator))

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'{memory_before} -> {memory_after}')
# 결과 : 14.0625 -> 14.0625 (메모리 사용량 그대로)

def increase(number: int = 0):
    while True:
        number += 1
        yield number

result = increase()
while True:
    data = input("Y/n >> ")
    if data == "Y":
        print(next(increase()))
    else:
        break
