s=set()
s1=set()
a=[1,3,7,2,4]
b=[2,4,7]
for i in a:
    s.add(i)
for j in b:
    s.add(j)
print(s)
for i in a:
    for j in b:
        if(i==j):
            s1.add(i)
print(s1)
