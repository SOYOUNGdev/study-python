# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트
# 전체 내용을 문자열로 가져오기: file.read()

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

# alice파일을 읽어온다. with 안에서는 file이라는 이름으로 해당 파일 사용할 것이다.
# 또한 with특성 상, file.close()를 작성하지 않아도 자동으로 해준다.
# read()를 사용하여 파일 전체를 하나의 문자열로 읽어온 뒤, lower()로 모두 소문자로 변경한다.
# 이를 content 라는 변수에 저장한다.
with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

# temp라는 빈 문자열을 미리 선언한다.
temp = ""
# content에 담겨있는 문자들이 하나씩 character에 담긴다.
for character in content:
    # 만약 character가 a~z사이의 문자라면
    if 'a' <= character <= 'z':
        # temp에 해당 문자를 연결하고
        temp += character
        # 밑의 코드는 실행하지 않게 하기 위해 continue를 사용한다.
        continue
    # character가 a~z사이의 문자가 아닌 특수문자라면
    # 그 자리는 공백으로 연결해준다.
    temp += " "

# 이제 temp는 a~z사이의 문자와 공백만이 결합되어있는 문자열이다.
# 이를 content에 다시 담아준다.
content = temp

# words라는 리스트를 만든다.
# 이 리스트에는 content에서 공백을 기준으로 나눈 단어들 중,
# 단어의 길이가 1보다 긴 단어들만 들어가 있다.
# 즉, s, a 와같은 단어들은 해당 리스트에 저장되지 않는다.
words = [
    word
    for word in content.split()
    if len(word) > 1
]

# result라는 빈 dict를 만든다.
# 현재 reuslt에는 key,value 둘 다 비어있다.
result = {}
# 단어들만 저장되어있는 리스트(words)에서 단어를 하나씩 받아온다.
for word in words:
    # 만약, 해당 단어와 같은 단어가 result dict의 key값에 존재한다면,
    # 해당하는 value값을 1증가시킨다.
    if result.get(word) is not None:
        result[word] += 1

    # 해당 단어가 result dict의 key값에 존재하지 않는다면,
    else:
        # {key: word, value: 1}로 result dict에 추가해준다.
        result[word] = 1

# 새로운 result dict를 만든다.
# 이 dict에는 원래있던 result dict에서 단어를 하나씩 받아와서
# 그 단어가 key값인 value값이 100이상이라면
# 그 단어는 content에 100번 이상 나왔다는 것이다.
# 따라서, value가 100 이상인 단어들만 새로운 result에 dict 형태로 저장한다.
# key(100이상인 단어) : value(횟수)
result = {
    word: result[word]
    for word in result
    if result[word] >= 100
}

# dict는 sorted 하게되면, 키 값을 기준으로 정렬된다.(list타입으로 정렬됨)
# 때문에, key에 result.get이라는 함수를 전달하여, value값을 기준으로 정렬할 수 있게 해야한다.
# 횟수가 높은 단어부터 -> 낮은 단어 순으로 출력해야하므로
# reverse=True 를 사용해 내림차순으로 정렬해주어야한다.
sorted_key = sorted(result, key=result.get, reverse=True)
# print(type(sorted_key)) # <class 'list'>
# 정렬된 list에서 키값을 하나씩 받아와
for key in sorted_key:
    # 해당 key값과 value값을 출력한다.
    print(key, result[key])

#
#
#
# def change(data):
#     return data * -1
#
# datas = [1, 2, 3, 4]
#
# print(sorted(datas, key=change))

# print(list({"A": 1, "B": 2, "C": 3}))
