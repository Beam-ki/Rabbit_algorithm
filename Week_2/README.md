2주차 문제 풀이
1.두 정수 사이의 합
```python
def solution(a, b):
    answer=0
    if a<b:
        for i in range(a,b+1):
            answer +=i        
    elif a>b:
        for i in range(b,a+1):
            answer +=i
    elif a==b:
        answer=a
    return answer
```
문제의 조건에 a,b 두 정수만 주어지고 a가 클지 b가 클지모르기때문에 if문으로 시작해서 a가 더작을경우에는  a~b+1까지 for 문을 돌려서 answer에 i를 차곡 차곡 더해주었고 a가 더 클경우에는 b,a+1로 작성했다. 끝으로 a와 b의 수가 같을경우에는 둘중 아무거나 rerturn 하라 했기때문에 a를 return시켜주었다.



2.문자열을 정수로 바꾸기
```python
def solution(s):
    answer=int(s)
    return answer
```
아마이건 파이썬이라 쉽게 풀린거 같은데.쉬웠다 설마하면서 해봤는데 바로풀려서 당황:

3.정수 내림차순으로 배열
```python
def solution(n):
    list=[]
    for i in map(int,str(n)):
        list.append(i)
        A=sorted(list,reverse=True)
        answer=''.join(map(str, A))
    return int(answer)
```
list안에다가 map()을이용해서 하나씩 분해해주고 append를 통해 하나씩 추가해주었다 그다음에 내림차순으로 정렬을 해야되는데
오름차순은 sort고 내림차순은 reverse 니 reversed로 될줄알았는데 안됐다 sorted가 자동완성되길래 구글링해보니 sorted()안에 reverse=false가 있어서 내림차순으로 하고싶으면 reverse=True로 바꿔서 사용해야된다. 내림차순으로 정렬후에 join()함수를이용해서 합쳐주었다.
https://velog.io/@qhsh866/Python-split-join-map-%EB%AC%B8%EC%9E%90%EC%97%B4-%EA%B4%80%EB%A0%A8-%ED%95%A8%EC%88%98-%EC%A0%95%EB%A6%AC

4.나머지가 1이되는 수  찾기
```python
def solution(n):
    answer=[]
    for i in range(1,n):
        if n % i ==1:
            answer.append(i)
    return answer[0]
```
나는 이렇게 풀었다. 단순 i 만 return 하게되면  i의 값이 여러개 나오게되어서 첫번째 요소만 return하게했다
```python
def solution(n):
    for i in range(1,n):
        if n % i ==1:
            return i
```
그런데 이답도 맞는다고는 한다 이렇게되면 i의 값이 여러개 들어가서 틀린것이 아닌가?

5.음양더하기
```python
def solution(absolutes, signs):
    answer=0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer +=absolutes[i]
        else:
            answer -=absolutes[i]
    return answer
```
이문제는 1분만에 푼내용인데 signs 에 있는 true와 false 단순 string이 아닌 boolean 연사자임을 생각하지 않고있었다.(문제를 꼼꼼히 읽읍시다!)
하여튼 vscode상으로는 정답이 나왔는데 프로그래머스웹에서는 스트링으로 인식해버려서 계속해서 오답이였다
조금더 찾아보니 실제로 나처럼 "true"문자열로 주어서 전전긍긍하신 분들이 많은 거같다.
문제풀이 들어가보면 absolutes 와 signs 1:1 대칭으로 True 면 양수 false면 음수 로 absolutes의 숫자들을 모두합한값을 리턴 주면된다
이런 유형의 문제들을 꾸준히 풀었기때문에 다행이다. i ==true 면 answer에 더해주고 아니라면 뺴준다고 한게끝이다
다풀고 다른사람들의 정답으보니 굳이 ==True 를 붙이지 않고 
if signs[i]: 해도 True인지 false 인지 알려준다고한다. 


6.예산
```python
def solution(d, budget):
    answer=0
    d.sort()
    for i in range(len(d)):
        if budget >= d[i]: 
            answer +=1
            budget -= d[i]
        else:
            break
    return answer
```
지난 문제들과 매우 유사한 유형의 문제들이였고 어렵지 않았다
문제 조건중하나가 정해진 budget 내에서 최대한 많은 팀들에게 나누어 주라했으니 우선 d를 오름 차순으로 정렬하는게 먼저라고 생각했다.
이후 for문을 돌려서 d[0] 번째~ i번쨰까지 budget을 차례대로 뺴주었다 answer에 팀수를 구하는거니 한번 뺼떄마다 answer 가 하나씩 늘어난다.
반복하다가 budget이 d[i]보다 작아진다면 멈추고 answer를 리턴해준다  
다른 사람이 쓴코드를 보니 어렵다..내가작성한코드가 가장 나은거같다

7.k번쨰 수
```python
def solution(array, commands):
    answer=[]
    for i in commands:
        A=array[i[0]-1:i[1]]
        A.sort()
        answer.append(A[i[2]-1])
    return answer
```
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer=[5, 6, 3]
슬라이싱을 이용해서 풀었다. commands [a,b,c]는 a번쨰부터 b번쨰까지 잘라서 오름차순으로 정렬했을때  c번쨰 수를 answer에 담아주면된다.
i는 첫번째 commands에있는 2-1:5번째까지 슬라이싱해서 A에 담아준뒤 sort이용해서 오름차순으로 정렬해준뒤 commands의 2번째 요소에서 1을뺸숫자를 answer에 담아주는것을 commands갯수만큼 반복한다. -1를 써준이유는 첫번쨰요소는 [0]이기때문에 해주었다.
풀떄는 뭔가 신들린듯이 풀었는데 해설하려고하니 갑자기 어떻게 이렇게썻는지 헷갈리기시작한다..

8.같은 숫자는 싫어.
```python
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] !=arr[i-1]:
            answer.append(arr[i])
        return answer
```
arr= [1,1,3,3,0,1,1]	
answer=[1,3,0,1]
같은 숫자를 제거하되 앞에있는숫자와 다르다면 출력해준다. 맨처음에는 i+1로 접근했다가 마지막 집합체를 구분짓지않고 끝내서 생각의 방식을 바꾸었다.

9.실패율
```python
N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]	
result=[3,4,2,1,5]
# n단계 실패율 구하기 = n/range(len(stages))
#result= 실패율 높은 n단계부터 낮은 n단계까지 나열 (내림차순)
stages.sort() #오름차순
print(stages) #[1, 2, 2, 2, 3, 3, 4, 6]
# 1단계는 1/8 2단계는 3/7 3단계는 2/4 4단계는 1/2 5단계는 0/1
A=0
for i in range(len(stages)):
    # print(range(len(stages))) #총길이 8
    if  7 >= i >= 0:
        A +=stages.count(i+1)
        # print(A)
        print(stages.count(i+1)/(len(stages)))
    # elif 7 >= i >= 1:
        # A +=stages.count(i+1)
        # print(len(stages)-A)
        # print(stages.count(i+1)/(len(stages)-A))   
    elif A == 8:
        break
        # A +=stages.count(i+1)
        # print(stages.count(i+1)/(len(stages)-A))
    # elif A == 8:
    #     break

```
못풀었다. 하나씩 print했음에도 불구하고 분명 조금만 손보면 될거같은데 A가 8이되면 멈추게했음에도 불구하고 계속 분모가 0인 에러가 나오게된다.
