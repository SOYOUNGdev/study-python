# # fish.txt
# # 사용자에게 입력받은 물고기를 fish.txt에 작성한다.
# # 사용자가 q를 입력하면, fish.txt의 전체 내용을 삭제한다.
# # 사용자가 r을 입력하면, fish.txt의 전체 내용을 콘솔에 출력한다.
#
# title = 'q: 삭제, r: 읽기'
# message = '물고기: '
#
# while True:
#     fish = input(title + '\n' + message)
#
#     if fish == 'q':
#         with open('fish.txt', 'w', encoding='utf-8') as file:
#             pass
#
#     elif fish == 'r':
#         try:
#             with open('fish.txt', 'r', encoding='utf-8') as file:
#                 line = None
#                 while line != '':
#                     line = file.readline()
#                     print(line, end='')
#             break
#         except FileNotFoundError:
#             print('경로를 다시 확인해주세요.')
#
#     else:
#         with open('fish.txt', 'a', encoding='utf-8') as file:
#             file.write(fish + '\n')
#


# 고등어를 참치로 수정하기
fishes = ""

# 고등어가 있다면 해당 문자열 자리에 참치 연결하기
with open('fish.txt', 'r', encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.readline()
        if line == '고등어\n':
            fishes += '참치\n'
            continue
        fishes += line

# 덮어쓰기
with open('fish.txt', 'w', encoding='utf-8') as file:
    file.write(fishes)

# 원본 파일 출력하여 수정본 확인하기
with open('fish.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))