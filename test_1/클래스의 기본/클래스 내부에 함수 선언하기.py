class student:
    def __init__(self, name, math, english, korean):
        self.name = name
        self.math = math
        self.english = english
        self.korean = korean
    
    def student_sum(self):
        """
        학생의 총점을 구하는 함수
        """
        return self.math + self.english + self.korean
    

    def student_average(self):
        """
        학생의 평균을 구하는 함수
        """
        return self.student_sum() / 3


    def student_string(self):
        return "{}\t{}\t{}".format(self.name, self.student_sum(), self.student_average())


Students = [
    student("ddd",14,34,44),
    student("dad",14,34,44)
]

for i in Students:
    print(i.student_string())