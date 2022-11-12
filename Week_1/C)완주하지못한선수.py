a=["marina", "josipa", "nikola", "vinko", "filipa"]
b=["josipa", "filipa", "marina", "nikola"]
# c=[x for x in b if x not in b]
# c= a-b
# print(c)
# c= set(c)
# print(c)
a.sort()
b.sort()
print(a)
print(a[0])
print(range(len(a)))
print(b)
for i in range(len(b)):
    if a[i] != b[i]:
        print(a[i])
print(a[len(a)-1])



# collections.Counters
# 임포트 필요
