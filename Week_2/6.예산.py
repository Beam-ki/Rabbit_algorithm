d=[1,3,2,5,4]
d.sort
budget=9
def solution(d, budget):
    answer=0
    for i in range(len(d)+1):
        if budget > d[i]: 
            budget -= d[i]
            answer +=1
        else:
            break
    return answer









print(solution(d,budget))
#최대한 많은 부서에게 지원해준다
#