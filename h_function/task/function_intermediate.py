# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'}
# ]
# # print(type(user_info[0]))
# # print(len(user_info))
# # print(user_info[0])
#
# # 방법1(강사님 코드)
# # 추가
# # 회원 번호는 자동 증가한다..
# number = 5
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': name})
#
# # 목록
# def select_all():
#     return user_info
#
# # 조회(번호로 조회)
# def select(number):
#     for user in user_info:
#         if user['number'] == number:
#             return user
#     return {}
#
# # 수정
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#     '''
#     select(kwargs.get('number'))['name'] = kwargs.get('name')
#
# # update(number= 1, name='han')
# # print(select_all())
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]
#
#
# # 방법1(내가 짠 코드)
# # 추가
# # 회원 번호는 자동 증가한다
# def insert(*, number, name):
#     '''
#
#     :param number: 회원 번호
#     :param name: 회원 이름
#     '''
#     user_info.append({'number': number, 'name': name})
#
# # insert(number=6, name='hong')
# # print(user_info)
#
# # 목록
# def list():
#     user_number = [user_info[i]['number'] for i in range(len(user_info))]
#     user_name = [user_info[i]['name'] for i in range(len(user_info))]
#     for i in range(len(user_info)):
#         print(f'{user_number[i]}, {user_name[i]}')
#
# # list()
#
# # 조회(번호로 조회)
# def find(number):
#     '''
#     :param number: 회원 번호
#     '''
#     num = number
#     for i in range(len(user_info)):
#         if user_info[i]['number'] == num:
#             return user_info[i]['name']
#
#     return None
#
# result = find(3)
# if result:
#     print(f'name is {result}')
# else:
#     print('일치하는 회원 없음')
#
# # 수정(번호로 이름 수정)
# def update_name(number):
#     '''
#
#     :param number: 회원 번호
#     '''
#     num = number
#     update_message = '수정할 이름 입력: '
#     update_ok_message = '수정 성공'
#     update_not_ok_message = '수정 실패(해당 회원 없음)'
#     for i in range(len(user_info)):
#         if user_info[i]['number'] == num:
#             user_info[i]['name'] = input(update_message)
#             return update_ok_message
#     return update_not_ok_message
#
# # result = update_name(3)
# # print(result)
# # list()
#
# # 삭제(번호로 삭제)
# def delete(number):
#     num = number
#     delete_ok_message = '삭제 완료'
#     delete_not_ok_message = '삭제 실패(해당 회원 없음)'
#     for i in range(len(user_info)):
#         if user_info[i]['number'] == num:
#             del user_info[i]
#             return delete_ok_message
#     return delete_not_ok_message
#
# result = delete(3)
# print(result)
# list()


# 실습2
post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# # 방법1(강사님 코드)
# # 추가
# number = 5
# def insert(**kwargs):
#     '''
#
#     :param kwargs: {'title: '게시글 제목', 'content': '게시글 내용', 'file': '파일의 경로'}
#     :return:
#     '''
#     global number
#     number += 1
#     post = {
#         'number': number,
#         'title': kwargs['title'],
#         'content': kwargs['content'],
#         'file': kwargs['file']
#     }
#
#     post_info.append(post)
#
# # 목록(최신순으로 조회)
# def select_all():
#     return post_info[::-1]
#
# # 조회(번호로 조회, 조회수 1증가)
# def read(number):
#     post = select(number)
#     post['read_count'] += 1
#     return post
#
# def select(number):
#     for post in post_info:
#         if post['number'] == number:
#             return post
#
#
# # 수정(번호로 정보 수정)
# def update(**kwargs):
#     post = select(kwargs.get('number'))
#     post['title'] = kwargs.get('title')
#     post['content'] = kwargs.get('content')
#     post['file'] = kwargs['file']
#
# # 삭제(번호로 삭제)
# def delete(number):
#    del post_info[post_info.index(select(number))]
#
# insert(title='테스트 제목6', content='테스트 내용6', file='')
# print(select_all())
# print(read(5))
# print(read(5))
# print(read(5))
# post = read(5)
#
# post['title'] = '수정된 제목'
# update(**post)
# print(read(5))
# delete(5)
# print(select_all())




# # 방법2(내가 짠 코드)
# # 추가(조회수는 전달받지 않고 기본값 0으로 설정)
# number = 5
# def insert(title, content, file, read_count=0):
#     global number
#     number += 1
#     post_info.append({'number': number, 'title': title, 'content': content, 'file': file, 'read_count': read_count})
#
# # insert(title='테스트 제목6', content='테스트 내용6', file='/usr/post/file/img005.png')
# # select_all()
#
# # 목록(최신순으로 조회)
# def select_all():
#     total_list = []
#     print(post_info[0].values())
#     for i in range(number):
#         new_list = list(post_info[i].values())
#         total_list.append(new_list)
#
#     print(total_list[::-1])
#
# # 검색(조회 수 증가 없이)
# def find(num):
#     for i in range(number):
#         if post_info[i]['number'] == num:
#             return post_info[i]
#
#     return {}
#
# # 조회(번호로 조회, 조회수 1 증가)
# def select_one(num):
#     find_post = find(num)
#     if find_post:
#         find_post['read_count'] += 1
#         return find_post
#     return {}
#
# # result = select_one(3)
# # result = select_one(3)
# # result = select_one(2)
# # select_all()
# # if result:
# #     print(result)
# # else:
# #     print('해당 번호의 게시글 없음.')
#
# # 수정(번호로 정보 수정)
# def update(num, **kwargs):
#     # print(type(kwargs))
#     # print(kwargs)
#     if 'title' in kwargs:
#         find(num)['title'] = kwargs.get('title')
#     if 'content' in kwargs:
#         find(num)['content'] = kwargs.get('content')
#     if 'file' in kwargs:
#         find(num)['file'] = kwargs.get('file')
#
#
# # update(3, title='수정된 제목3', content='수정된 내용3')
# # select_all()
#
#
# # 삭제(번호로 삭제)
# def delete(num):
#     del post_info[post_info.index(select_one(num))]
#
# # delete(1)
# # select_all()