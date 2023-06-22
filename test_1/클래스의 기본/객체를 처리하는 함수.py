def create_student(name,math,english):
    return{
        "name":name,
        "math":math,
        "english":english
    }

def student_sum(student):
    return student["english"]+student["math"]

def student_average(student):
    return student_sum(student) / 2

def student_string(student):
    print(student["name"],student["math"],student["english"],student_sum(student),student_average(student),sep="\t")


sutdents = [
    create_student("채승병",2,6),
    create_student("냥냥이",5,5)
]

student_string(sutdents[0])
student_string(sutdents[1])

'''
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

def student_get_sum(student):
    return student["korean"]+student["math"]+student["english"]+student["science"]

def student_get_average(student):
    return student_get_sum(student)/4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )

students = [
    create_student("윤인성",87,98,88,95),
    create_student("연하진",92,98,96,98),
    create_student("구지연",76,96,94,90),
    create_student("나선주",98,92,96,92),
    create_student("윤아린",95,98,98,98),
    create_student("윤명월",64,88,92,92)
]

print("이름","총점","평균", sep="\t")

for student in students:
    print(student_to_string(student))









def create_item(name, a,b,c,d,e):
    return{
    "name":name,
    "item_1":a,
    "item_2":b,
    "item_3":c,
    "item_4":d,
    "item_5":e
    }

def item_sum(item):
    return item["item_1"]+item["item_2"]+item["item_3"]+item["item_4"]+item["item_5"]

def item_average(item):
    return item_sum(item) / 5


def item_string(item):
    
    print(item["name"],item["item_1"],item["item_2"],item["item_3"],item["item_4"],item["item_5"],item_sum(item),item_average(item),sep="\t")


item_list = [
    create_item("채모씨",1,2,3,4,5),
    create_item("a모씨",1,2,3,4,5),
    create_item("b모씨",1,2,3,4,5),
    create_item("c모씨",1,2,3,4,5),
    create_item("d모씨",1,2,3,4,5)

]
print("이름","item_1","item_2","item_3","item_4","item_5","합","평",sep="\t")
for i in item_list:
    item_string(i)

'''