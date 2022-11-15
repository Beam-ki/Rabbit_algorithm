array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# answer=[5, 6, 3]
# def solution(array, commands):
answer=[]
for i in commands:
    print(i)
    print(array[i])
    A=array[i[0]-1:i[1]]
    print(A)
    A.sort()
    print(A)
        # print(A)
        # print(A[commands[2]-1])
    answer.append(A[i[2]-1])
    print(answer)
        # return answer