class Student:
    # static 변수
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    # 모든 학생의 상태가 공유되는 경우,
    # 굳이 self를 사용해서 객체로 접근할 필요가 없는 메소드이다.
    # 따라서 클래스로 직접접근해서 사용할 수 있게
    # 정적 변수와 같이 staticmethod를 사용해 메소드를 메모리에 바로 할당해준다.
    @staticmethod
    def print_start_time_of_study():
        print("9시 땡")
        Student.status = '공부 중'

han = Student(0,0,0)
hong = Student(0,0,0)
print(Student.status)

Student.print_start_time_of_study()
print(Student.status)