import time as t

class Student:
    """
    class Student에 클래스 선언부
    """
    def __init__(self, name, korean, math, english, science):
        print("생성됨")
        self.name = name
        print("name선언됨 name: {}".format(name))
        t.sleep(0.5)
        self.korena = korean
        print("korean선언됨 korean : {}".format(korean))
        t.sleep(0.5)
        self.math = math
        print("math선언됨 math: {}".format(math))
        t.sleep(0.5)
        self.english = english
        print("english선언됨 english: {}".format(english))
        t.sleep(0.5)
        self.science = science
        print("science선언됨 science: {}".format(science))
        t.sleep(0.5)

    def __del__(self):
        print("파괴 완료 파괴한 객체 : {}".format(self.name))


students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,97,94,90),
    Student("나선주",98,92,96,92)
]

print(students[0])
