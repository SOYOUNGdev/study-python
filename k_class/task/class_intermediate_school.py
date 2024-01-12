# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드
class School:
    # 기본 생성자
    # 매개변수로 해당 개체의 주소값(self)와
    # 학교이름, 지역, 학생 수, 선생님 수를 전달받는다.
    # 메모리 할당하여 해당 메모리에 해당 객체를 저장한다.
    def __init__(self, name, location, student_count=0, teacher_count=0):
        self.name = name
        self.location = location
        self.student_count = student_count
        self.teacher_count = teacher_count

    # 학교 정보 출력 함수(이름, 지역, 학생 수, 선생님 수)
    def print_info(self):
        print(f'학교 이름: {self.name}, 지역: {self.location}, 학생 수: {self.student_count}, 선생님 수: {self.teacher_count}')


# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드
class Teacher:
    # 기본 생성자
    # 매개변수로 해당 객체의 주소와(self)
    # 선생님 이름, 과목, 학교를 전달 받는다.
    # 이 때, school은 School클래스의 객체이다.
    def __init__(self, name, subject, school):
        self.name = name
        self.subject = subject
        self.school = school
        # Teacher 객체가 메모리에 할당되며 생성될 때 마다 해당 학교의 전체 선생님 수는 1 증가한다.
        self.school.teacher_count += 1

    # 선생님 정보 출력(선생님 이름, 과목)
    def print_info(self):
        print(f'선생님 이름: {self.name}, 과목: {self.subject}')
        # 해당 선생님이 가진 School타입의 객체로 접근하여 학교 정보 출력함수를 호출한다.
        # self.school.print_info()

    # 선생님이 해당 과목을 가르칠 때마다, 학생들의 능력 1 증가 하는 함수
    # 매개변수로 해당 선생님과 학생 리스트를 받는다.
    # 이 때, students는 Student 클래스의 객체들로 이루어진 리스트이며,
    # 각 객체들에는 학생 정보가 저장되어있다.
    def teach(self, students):
        # 리스트에서 학생을 한명씩 받아와서
        for student in students:
            # 각 학생의 능력을 1씩 증가시킨다.
            student.ability += 1



# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:
    # 기본 생성자
    # 매개변수로 생성된 객체의 주소와(self)
    # 학생이름, 학년, 학교, 선생님, 능력을 전달 받는다.
    # 이 때, 학교는 School클래스의 객체이고
    # 선생님은 Teacher클래스의 객체이다.
    # 따라서, 해당 객체에는 학교의 정보와 선생님의 정보가 저장되어있다.
    def __init__(self, name, grade, school, teacher, ability=0):
        self.name = name
        self.grade = grade
        self.school = school
        self.teacher = teacher
        self.ability = ability
        # Student클래스의 객체가 생성되며 메모리에 할당 될때 마다, 해당 학교의 전체 학생 수는 1증가된다.
        self.school.student_count += 1

    # 학생 정보 출력 함수
    def print_info(self):
        # 해당 객체로 접근하여 학생이름, 나이, 능력을 출력한다.
        print(f'학생이름: {self.name}, 학년: {self.grade}, 능력: {self.ability}')
        # 해당 객체(학생)에 저장되어있는 학교와 선생님 객체를 통해 각각의 출력함수를 호출한다.
        self.school.print_info()
        self.teacher.print_info()


school = School('영동고등학교', '서울')
teacher = Teacher('한동석', '컴퓨터', school)
students = [
    Student('홍길동', 1, school, teacher),
    Student('이순신', 1, school, teacher),
    Student('장보고', 2, school, teacher)
]

teacher.teach(students)
for student in students:
    student.print_info()








