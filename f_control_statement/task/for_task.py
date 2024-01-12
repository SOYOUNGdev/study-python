# 1~15까지 출력
# for i in range(15):
#     print(i + 1)

# 30~1까지 출력
# for i in range(30):
#     print(30 - i)

# 1~100까지 중 홀수만 출력
# for i in range(50):
#     print(i * 2 + 1, end=' ')

# 1~10까지 합 출력
# 0
# 0 + 1
# (0 + 1) + 2
# (0 + 1 + 2) + 3
# ...
# total = 0
# for i in range(10):
#     # total = total + i + 1
#     total += i + 1
# print(total)

# 1~n까지 합 출력
# message1 = '1~n까지의 합'
# message2 = 'n: '
# end = int(input(message1 + '\n' + message2))
#
# total = 0
# for i in range(end):
#     total += i + 1
#
# print(total)

# 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(12):
#     print(i % 4 + 3, end=' ')

# '1,235,500'를 1235500으로 출력
data = '1,235,500'
result = ''
for i in data:
    if i != ',':
        result += i

result = int(result)
print(result + 5)








