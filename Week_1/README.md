1주차 문제 풀이

1.짝수와 홀수
``` python
def solution(num):
    if (num % 2) == 0:
        answer="Even"
    else:
        answer="Odd"
    return answer
``` 
if 문을 통하여 몫을 나타내는 % 를 사용해서 0이면짝수(Even) 0이아니면 홀수(Odd)를 출력도록 만들었다.
난이도 下

2.평균 구하기
``` python
def solution(arr):
    sum_arr=sum(arr)
    return sum_arr/len(arr)
```
입력받은 배열을 arr에 담아서 sum(합계)된 배열을 sum_arr변수에 저장 (왜 했는지 모르겠다) 후 배열합/배열의길이 하여 배열의 평균을 구했다.
난이도 下
sum(arr)을 통해 이미 합산을 구했음에도 불구하고 왜 sum_arr에 저장했을까? 쓰다보니 본능적으로 적었다

3.자릿수 더하기
``` python
def solution(n):
    list=str(n)
    answer=[]
    for i in list:
        answer.append(int(i))
    return sum(answer)
```
생각보다 오류를 많이 만났다 입력받은 n을 하나씩 str형변환으로 뗴어낸뒤 list에 넣어서 배열의 합으로 구할 생각이였는데
for문을 돌리는 과정에서 실수는 for를 돌린 i를 str상태로 append한뒤 sum하려고 했던것이다.  

4.자연수 뒤집어 배열로 만들기
``` python
def solution(n):
    a = []
    n1=str(n)
    for i in reversed(n1):
        a.append(int(i))
    return (a)
```
3번 풀이와 비슷했다.다른점이있다면 for문을 reversed를 이용해서 뒤집어주었다는점

5.없는 숫자 더하기
``` python
def solution(numbers):
    b= [1,2,3,4,6,7,8,0,5,9]
    answer=[x for x in b if x not in numbers]
    return sum(answer)
```
꼼수(?)를 써서 풀었다. 문제조건에 numbers는 0~9사이의숫자라고하길래 임의로 0~9숫자를 전부다 가진 배열을 만든뒤 list끼리 뺄셈을 하는 방법이 있지 않을까 검색을 하였는데 너무나도 쉬운 방법이있었다 문제를 풀면서 약간의 편법이라고 생각했는데 가장 추천수가 많은 해결법을 보자마자 놀라웠다 ㅋㅋㅋ 
[x for x in b if x not in numbers] 에 대한 해석 -- 
b를 x만큼 돌린것을 x에 담고 담은 x를 다시 numbers에 x만큼 돌려서 numbers에 포함되어있지 않는 값 x를 배열에 담아준다 가 맞나요? 



6.숫자문자열과_영단어
``` python 
    def solution(s):
        answer = 0
        s = s.replace('zero', '0')
        s = s.replace('one', '1')
        s = s.replace('two', '2')
        s = s.replace('three', '3')
        s = s.replace('four', '4')
        s = s.replace('five', '5')
        s = s.replace('six', '6')
        s = s.replace('seven', '7')
        s = s.replace('eight', '8')
        s = s.replace('nine', '9')
        return int(s)
```
맨처음에는 for문을 돌려서 하나씩조건문을 거는방식으로 하려다가 너무 코드가 길어지고 난잡해질거같아서 문자열 변환이라고 구글링했던결과
replace라는 함수를 알수있었다. 사실 위 와같은 답도 정답이긴하지만 프로그래밍상 더 좋은 방법이있을거같았다 (아마 ('','') 이부분을 for문으로 돌리면 한줄또는 두줄로 가능할지도?) 다른사람들의 코드를보니 relpace 라는 함수보다는 items()라는 함수를 딕셔너리형태로 깔끔하게 작성했다

items()는 key,value값을 튜플로 묶어서 리스트형식으로 반환해준다.
items()함수가 내가 코드를 작성한뒤 생각했던 방식이였다 같이 replace를 사용햇지만 for 문을 쓰고안쓰고 코드의 길이가 세배 이상 간결해졋다.


7.
``` python
def solution(participant, completion):
    answer = [x for x in participant if x not in completion]
    return ','.join(answer)
```
첫 번쨰 시도 5번문제와 비슷하게 풀어보려했으나 일부는 검증과정에서 오류가났다
이유는 동명이인의 참가자가 있을때 한명만 들어왔다면 participant에서 두명다 지워버리기 떄문이다 한개만 지워야되는데
방법을 계속고민했다 set,sort,difference  차집합 등.. 그러나 문자열이라서 list형식이라는 이유로 계속 실패하다가 
이번 문제의 카테고리가 해시인것을 보고 해시가 무엇이고 이문제에 어떻게 사용할지 찾았다.

결국 해시이해도 못했고 원하는 답도 찾지 못했다.
위에 시도해봤던 과정중 가장 근접했다고 생각했던것은 sort로  하나씩 비교하고 아닌것을 반환하자 해서 
for 문을 돌리기시작했다
``` python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
```
