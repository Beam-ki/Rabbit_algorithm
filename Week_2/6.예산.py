d=[1,3,2,5,4]
d.sort
budget=9
def solution(d, budget):
    for i in range(len(d)+1):
        if budget > d[i]: 
            budget -= d[i]
        else:
            return i+1
    return budget









print(solution(d,budget))
#최대한 많은 부서에게 지원해준다
#