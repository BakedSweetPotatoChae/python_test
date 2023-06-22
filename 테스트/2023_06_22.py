a=solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])



def solution(players, callings):
    answer = [players]
    print()
    for i in range(len(callings)):
        print(answer.index(callings[i]))
    return answer