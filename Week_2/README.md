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