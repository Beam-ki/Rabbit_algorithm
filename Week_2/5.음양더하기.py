absolutes=[4,7,12]	
signs=[True,False,True]


def solution(absolutes, signs):
    answer=0
    for i in range(len(absolutes)):
        if signs[i]:
            answer +=absolutes[i]
        else:
            answer -=absolutes[i]
    return answer
# print(solution([4,7,12], [True,False,True]))
print(solution(absolutes, signs))

# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
#해석 이필요한 숏코딩.