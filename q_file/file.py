# 절대 경로: 대한민국 서울시 강남구 역상동 123-123 103동 203호
# 어떤 위치에 있든 상관없이 찾아갈 수 있는 경로
# C:/a/b, D:/User/ted, ..

# 상대 경로: 직진해서 좌회전 후 오른쪽 건물
# 현재 위치에 따라 변경되는 경로
# ./ : 현재 경로, ../ : 이전 경로, ./src/images, ../../a/b, src/images

# 파일 생성하기
# 'w'모드로 작성하는 순간 파일에 있는 바이트가 모두 0이 된다.
# file = open('food.txt', 'w', encoding='utf-8')
# # write를 하면 알아서 flush가 된다.
# file.write('부대찌개\n')
# file.write('햄버거\n')
# # 파일을 닫아주어 후에 변경이나 삭제가 가능하도록 한다.
# file.close()

# # 파일 추가하기
# file = open('food.txt', 'a', encoding='utf-8')
# file.write('피자\n')
# file.close()

# # 파일 읽기
# try:
#     file = open('food.txt', 'r', encoding='utf-8')
#     # print(file.readlines())
#     # for i in range(10):
#     #     # print(file.readline(), end='')
#     #     print(i + 1)
#     #     if file.readline() == '':
#     #         print('다 읽었어요!')
#     line = None
#     while line != '':
#         line = file.readline()
#         print(line, end='')
#
#     file.close()
# except FileNotFoundError:
#     print('경로를 다시 확인해주세요.')

# with를 사용하면, 자동으로 file이 close된다.
# with open('food.txt', 'r', encoding='utf-8') as file:
#     print(file.readlines())


# 수정
# 1. 파일 읽으면서 해당 문자열이 있는지 검사, 있다면 수정. 미리 만들어둔 빈 문자열에 연결한다.
content = ""
with open('food.txt', 'r', encoding='utf-8') as file:
    line = None
    while line != '':
        # 한 줄을 line에 담기
        line = file.readline()
        # 담은내용이 찾고 있는 햄버거 일 경우
        if line == '햄버거\n':
            # content에 치킨으로 변경해서 담기
            content += '치킨\n'
            # 치킨 뒤에 햄버거를 연결하지 않게끔 하기 위해 continue 사용
            continue
        # 수정 대상이 아닌 문자열은 그대로 담기
        content += line

# 2. 기존의 내용을 수정 완료된 문자열로 덮어쓴다.('w')
with open('food.txt', 'w', encoding='utf-8') as file:
    file.write(content)

# 3. 원본 파일의 내용 확인
with open('food.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))