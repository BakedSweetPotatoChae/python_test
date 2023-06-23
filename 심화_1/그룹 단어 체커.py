N = int(input())

cnt = N

# 처음 받은 입력값 만큼 실행 시킨다.
for i in range(N):
    #word에 값을 입력음
    word = input()
    for j in range(0, len(word)-1):
        #다음과 같은 경우 pass 그러지 못하면 elif 문으로 문장에 존제하는지 여부를 확인 있으면 기존 인자에 차감
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)