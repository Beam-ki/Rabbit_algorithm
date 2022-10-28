1주차 문제 풀이

1.짝수와 홀수
def solution(num):
    if (num % 2) == 0:
        answer="Even"
    else:
        answer="Odd"
    return answer
if 문을 통하여 몫을 나타내는 % 를 사용해서 0이면짝수(Even) 0이아니면 홀수(Odd)를 출력도록 만들었다.
난이도 下

2.평균 구하기
def solution(arr):
    sum_arr=sum(arr)

    return sum_arr/len(arr)
입력받은 배열을 arr에 담아서 sum(합계)된 배열을 sum_arr변수에 저장 (왜 했는지 모르겠다) 후 배열합/배열의길이 하여 배열의 평균을 구했다.
난이도 下
sum(arr)을 통해 이미 합산을 구했음에도 불구하고 왜 sum_arr에 저장했을까? 쓰다보니 본능적으로 적었다

3.자릿수 더하기
def solution(n):
    list=str(n)
    answer=[]
    for i in list:
        answer.append(int(i))
    return sum(answer)

생각보다 오류를 많이 만났다 입력받은 n을 하나씩 str형변환으로 뗴어낸뒤 list에 넣어서 배열의 합으로 구할 생각이였는데
for문을 돌리는 과정에서 실수는 for를 돌린 i를 str상태로 append한뒤 sum하려고 했던것이다.  
질문)print(sum(answer))했더니 차례대로나오는대도 답이 맞는가?

4.자연수 뒤집어 배열로 만들기
def solution(n):
    a = []
    n1=str(n)
    for i in reversed(n1):
        a.append(int(i))
    return (a)

3번 풀이와 비슷했다.다른점이있다면 for문을 reversed를 이용해서 뒤집어주었다는점

5.없는 숫자 더하기

def solution(numbers):
    b= [1,2,3,4,6,7,8,0,5,9]
    answer=[x for x in b if x not in numbers]
    return sum(answer)

꼼수(?)를 써서 풀었다. 문제조건에 numbers는 0~9사이의숫자라고하길래 임의로 0~9숫자를 전부다 가진 배열을 만든뒤 list끼리 뺄셈을 하는 방법이 있지 않을까 검색을 하였는데 너무나도 쉬운 방법이있었다 문제를 풀면서 약간의 편법이라고 생각했는데 가장 추천수가 많은 해결법을 보자마자 놀라웠다 ㅋㅋㅋ 
[x for x in b if x not in numbers] 에 대한 해석 -- 
b를 x만큼 돌린것을 x에 담고 담은 x를 다시 numbers에 x만큼 돌려서 numbers에 포함되어있지 않는 값 x를 배열에 담아준다 가 맞나요? 