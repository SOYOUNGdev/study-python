name_list = []
price_list = []

title = "카페"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
# update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

# 몇 번 반복할지 모르니까 while문 사용
while True:
    # 이미 존재하는 상품인지 여부를 알기 위해 count 변수 사용
    count = 0
    # 사용자가 입력한 번호(1~6)를 number라는 변수에 저장한다.
    number = int(input(title + '\n' + menu))

    # 나가기
    if number == 6:
        break
    # 추가하기
    elif number == 1:
        # 사용자에게 입력받은 새로운 상품명과 가격을 각각 new_name과 new_price라는 변수에 저장한다.
        new_name, new_price = input(append_message + '\n').split(" ")
        # 가격은 문자열이 아닌 정수이므로 변환하여 다시 저장해준다.
        new_price = int(new_price)

        # 만약 현재 목록에 아무것도 없다면
        if len(name_list) == 0:
            # 상품명은 name_list에 추가를
            name_list.append(new_name)
            # 가격은 price_list에 추가한다.
            price_list.append(new_price)
        # 목록에 하나의 상품이라도 있다면,
        else:
            # 목록에 있는 상품명을 하나씩 가지고와서
            for i in range(len(name_list)):
                # 사용자가 추가하기 위해 입력한 상품명과 일치하는지 검사한다.
                # 일치하는 상품이 있다면,
                if name_list[i] == new_name:
                    # count의 수를 늘린다
                    count += 1
                    # 이미 존재하는 상품이므로 해당 오류 메세지를 저장한다.
                    result_message = append_error_message + '\n'
                    # 존재하는 상품이라면 무조건 count=1 이므로
                    # 존재하지 않을 경우의 코드는 실행하지 않기 위해 continue를 사용한다.
                    continue
            # 만약 count=0 이라면 사용자가 입력한 상품명과 동일한 상품명이 name_list에 존재하지 않는다는 것이다.
            if count == 0:
                # 따라서 사용자가 입력한 상품명은 name_list에,
                name_list.append(new_name)
                # 사용자가 입력한 가격은 price_list에 저장한다.
                price_list.append(new_price)

    # 수정하기
    elif number == 2:
        # 사용자에게 입력 받은 상품명을 before_update_name이라는 변수에 저장한다.
        before_update_name = input(search_name_message_for_update + '\n')
        # 목록에 있는 상품명을 하나씩 가지고 와서
        for i in range(len(name_list)):
            # 수정하고자 하는 상품명과 일치하는 상품이 목록에 있다면,
            if name_list[i] == before_update_name:
                # count의 수를 늘리고,
                count += 1
                # 사용자에게 입력받은 수정할 상품명과 가격을 각각 update_name과 update_price에 저장한다.
                update_name, update_price = input(update_message + '\n').split(" ")
                # 가격은 정수이므로 형변환하여 다시 저장한다.
                update_price = int(update_price)
                # 해당 상품의 가격을 수정해준다.
                name_list[i] = update_name
                price_list[i] = update_price
                # 존재하지 않을 경우의 코드는 실행하지 않기 위해 continue를 사용한다.
                continue
        # 수정하고자 하는 상품명과 일치하는 상품이 목록에 없다면,
        if count == 0:
            # 해당 오류 메세지를 저장한다.
            result_message = update_error_message + '\n'

    # 삭제하기
    elif number == 3:
        # 삭제하고자 하는 상품명을 사용자에게 입력받아 delete_name 변수에 저장한다.
        delete_name = input(delete_message + '\n')
        # 목록에 있는 상품명을 하나씩 가지고 와서
        for i in range(len(name_list)):
            # 입력한 상품명과 일치하는 상품이 목록에 존재한다면
            if name_list[i] == delete_name:
                # count + 1 해주고
                count += 1
                # 목록에 있던 상품명과 가격을 삭제한다.
                name_list.remove(delete_name)
                price_list.remove(price_list[i])
                # 존재하지 않을 경우의 코드는 실행하지 않기 위해 continue를 사용한다.
                continue
        # 목록에 존재하지 않는 상품명을 입력하였다면,
        if count == 0:
            # 해당 오류를 오류 메세지에 저장한다.
            result_message = delete_error_message + '\n'

    # 검색하기
    elif number == 4:
        # 상품명(1)과 가격(2) 중 사용자가 입력한 검색 수단을 정수로 변환하여 search_number에 저장한다.
        search_number = int(input(search_menu))

        # 상품명으로 검색
        if search_number == 1:
            # 사용자가 입력한 검색 상품명을 search_name에 저장한다.
            search_name = input(search_name_message)
            # 목록에 있는 상품명을 하나씩 가지고 와서
            for i in range(len(name_list)):
                # 사용자가 입력한 상품이 목록에 존재한다면
                if name_list[i] == search_name:
                    # count + 1 해준다
                    count += 1
                    # 해당 인덱스를 가진 상품명과 가격을 출력해준다.
                    print(f'상품명은 {name_list[i]}이며, 가격은 {price_list[i]}원 입니다')
                    # 존재하지 않을 경우의 코드는 실행하지 않기 위해 continue를 사용한다.
                    continue
            # 검색 상품이 목록에 없다면
            if count == 0:
                # 해당 오류를 오류 메세지에 저장한다.
                result_message = search_name_error_message + '\n'

        # 가격으로 검색
        elif search_number == 2:
            # 사용자가 입력한 가격을 정수로 변환하여 search_price에 저장한다.
            search_price = int(input(search_price_message))
            # 검색 오차가 50% 이므로
            # 최솟값은 입력한 가격 * 0.5
            # 최댓값은 입력한 가격 * 1.5
            min_search_price = search_price * 0.5
            max_search_price = search_price * 1.5
            # 목록에 있는 가격을 하나씩 가지고 와서
            for i in range(len(price_list)):
                # 해당 목록에 있는 가격이 최솟값과 최댓값 사이에 있다면
                if min_search_price <= price_list[i] <= max_search_price:
                    # count + 1 한다.
                    count += 1
                    # 해당 인덱스의 상품명과 가격을 출력한다.
                    print(f'상품명은 {name_list[i]}이며, 가격은 {price_list[i]}원 입니다')
                    # 존재하지 않을 경우의 코드는 실행하지 않기 위해 continue를 사용한다.
                    continue
            # 목록에 있는 가격이 최솟값과 최댓값 사이에 존재하지 않는다면
            if count == 0:
                # 해당 오류를 오류메세지에 저장한다.
                result_message = search_error_message + '\n'


    # 목록보기
    elif number == 5:
        # 상품명이 담겨있는 리스트의 길이가 0이라면
        if len(name_list) == 0:
            # 목록이 존재하지 않는다는 메세지를 출력한다
            print(no_item_message + '\n')
            # 목록이 존재할 경우의 코드는 실행하지 않기 위해 continue를 사용한다
            continue
        # 상품 리스트의 길이 만큼 반복
        for i in range(len(name_list)):
            # 해당 인덱스의 상품명과 가격을 출력한다.
            print(name_list[i], price_list[i])

    # 1~6 이외의 숫자 입력 시, 해당 오류 메세지 저장
    else:
        result_message = error_message + '\n'

    print(result_message)
    result_message = ""