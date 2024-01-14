import datetime

def log_time(original_function):
    def logging(*args, **kwargs):
        self, money = args
        error_code = kwargs.get('error_code')

        with open('log.txt', 'a', encoding='utf-8') as file:
                if not error_code:
                    # print(original_function.__name__)
                    # print(original_function)
                    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                    # 원래 함수가 출금이면, 잔액 - 출금액
                    if original_function.__name__ == 'withdraw':
                        file.write(f'예금주: {self.user_name}\t계좌번호: {self.user_account}\t잔액: {self.user_balance - money}\t거래시간: {now}\n')
                    # 원래 함수가 입금이면, 잔액 + 입금액
                    else:
                        file.write(f'예금주: {self.user_name}\t계좌번호: {self.user_account}\t잔액: {self.user_balance + money}\t거래시간: {now}\n')
                else:
                    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                    file.write(f'{error_code}\t예금주: {self.user_name}\t{now}\n')

        return original_function(*args, **kwargs)

    return logging
