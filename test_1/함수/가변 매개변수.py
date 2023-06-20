'''
def 함수이름(매개변수, 매개변수2, ... *가변 매개변수):
    문장
'''

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)

print_n_times(3,"안녕하세요", "즐거운", "파이썬")