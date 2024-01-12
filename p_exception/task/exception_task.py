# 캐릭터 닉네임을 정할 때, 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여, 발생 시 안내 메세지까지 출력하기

class NickNameError(Exception):
    def __str__(self):
        return "닉네임에는 비속어를 사용할 수 없습니다."

def check_nickname(nickname: str):
    bad_words = ['바보', '멍게', '해삼', '운영자']
    if any(bad_word in nickname for bad_word in bad_words):
        raise NickNameError

nickname = input("닉네임: ")
try:
    check_nickname(nickname)
    print(f'어서오세요 {nickname}님')

except NickNameError as e:
    print(e)
