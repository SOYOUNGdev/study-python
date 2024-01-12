# Comprehension(컴프리헨션: (어떤 뜻을) 내포[포함])
# 반복하거나 특정 조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension
# [표현식 for 항목 in iterator (if 조건)]
# number_list = [1, 2, 3, 4]
# result_list = [number * 3 for number in number_list]
# print(result_list)

# number_list = [1, 2, 3, 4]
# # [6, 12]
# result_list = [number * 3 for number in number_list if number % 2 == 0]
# print(result_list)

# [표현식 if 조건 else 표현식 for 항목 in iterator]
# [1, 6, 3, 12]
# number_list = [1, 2, 3, 4]
# result_list = [number * 3 if number % 2 == 0 else number for number in number_list]
# print(result_list)

# 아래의 list에서 '양수'만 추출한 뒤 새로운 list에 담기
# number_list = [10, 20, 30, -20, -3, 50, -70]
# result_list = [number for number in number_list if number > 0]
# print(result_list)

# n개의 0으로만 채워진 list
# message = '생성할 list의 칸 수: '
# length = int(input(message))
# # result_list = [0 for i in range(length)]
# # print(result_list)
# result_list = [0] * length
# print(result_list)

# 제곱(a ** 2)의 결과가 10보다 큰 결과만 담은 list
# number_list = [1, -2, 3, -4, 5]
# result_list = [number for number in number_list if number ** 2 > 10]
# print(result_list)

# 0~9까지 중 3의 배수만 담은 list
# result_list = [i for i in range(10) if i % 3 == 0]
# print(result_list)
