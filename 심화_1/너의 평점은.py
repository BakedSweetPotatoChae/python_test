all_Grades = 1
class subject:
    
    def __init__(self, subject_name,  subject_grade, Grades):
        self.subject_name = subject_name
        self.Grades = Grades
        print(subject_grade)
        if(Grades == "A+"):
            self.subject_grade_score = 4.5
            print(4.5)
        elif(Grades == "A0"):
            self.subject_grade_score = 4.0
            print(4.0)
        elif(Grades == "B+"):
            self.subject_grade_score = 3.5
            print(3.5)
        elif(Grades == "B0"):
            self.subject_grade_score = 3.0
            print(3.0)
        elif(Grades == "C+"):
            self.subject_grade_score = 2.5
            print(2.5)
        elif(Grades == "C0"):
            self.subject_grade_score = 2.0
            print(2.0)
        elif(Grades == "D+"):
            self.subject_grade_score = 1.5
            print(1.5)
        elif(Grades == "D0"):
            self.subject_grade_score = 1.0
            print(1.0)
        elif(Grades == "F"):
            self.subject_grade_score = 0.0
            print(0.0)

        self.subject_grade = subject_grade
    
    def required_courses(self):
        return self.subject_grade * self.subject_grade_score / all_Grades
    
subjects = [
    subject("dd","A+", 3.0)
]

print(subjects[0].required_courses())