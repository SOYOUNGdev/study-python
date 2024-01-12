# 1.
    # try:
    #     number = int(input('정수를 입력하세요.'))
    #
    # except ValueError as e:
    #     print('정수만 입력해주세요~!')
    #
    # print('반드시 실행되어야 하는 문장')

#2.
    # try:
    #     print(10 / 0)
    #
    # # except:
    # # except Exception:
    # # except ZeroDivisionError:
    # except ZeroDivisionError as e:
    #     print('0으로 나누는 오류 발생')
    #     print(e)
    #     # 결과 : division by zero
    #     # 주소값이 나오지 않고 string이 나옴. -> 모든 에러들은 __str__()을 재정의했다.


# 3.
# datas = [1, 2, 3]
#
# try:
#     print(datas[3])
#     # 위의 문장에서 오류가 발생하지 않는다면 해당 코드가 실행된다.
#     print('오류가 없어요1')
#
# except ValueError:
#     pass
#
# except IndexError:
#     print('인덱스를 확인인해주세요!')
#
# else:
#     # try문에서 오류가 발생하지 않는다면 해당 코드가 실행된다.
#     print('오류가 없어요2')
#
# finally:
#     print('오류가 있든 없든 반드시 실행되어야 하는 문장')



class BadWordError(Exception):
    def __str__(self):
        return "비속어는 사용할 수 없습니다."

def check_bad_word(message: str):
    if '멍청이' in message:
        raise BadWordError

chat = input('채팅: ')
try:
    check_bad_word(chat)
    print(chat)

except BadWordError as e:
    print(e)
