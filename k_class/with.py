class NameCard:
    def print_info(self, name):
        print(name)

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def __del__(self):
        print('del')

# with 문은 enter()부터 사용한다.
# with문이 종료된 후, exit() 실행
# 그 후, del() 실행. 즉, 소멸자가 자동으로 실행되어서 with문이 종료되면 객체가 메모리에서 다 해제된다.
with NameCard() as name_card:
    name_card.print_info('임소영')

# 결과
# enter
# 임소영
# exit
# del