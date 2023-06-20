'''
def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "줄거운 파이썬","프로그래밍")
'''

#위 프로그램은 오류가 발생한다. 이유는 프로그램을 그대로 읽어보면 n에 "안녕하세요"가 들거아고 뒤에 value에 차래대로 "즐거운","파이썬" 이 들어가서 이다
'''
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요","즐거운", "파이썬 프로그래밍",3)
'''
#위 프로그램은 실행만 되지만 이미 뒤에 가변 매개변수를 넣은 상태이므로 앞 문장부터 3까지 전부 values에 넣는다.

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕","하세요",n=2)
