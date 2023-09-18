a=eval(input())
b=eval(input())
a=sorted(a)
b=sorted(b)
c=[]
d=[]
for i in a:
    if(i in b):
        c.append(i)
print("intersection is",c)
for i in a:
    if(i in b):
        d.append(i)
    else:
        d.append(i)
for i in b:
    if(i not in a):
        d.append(i)
d=sorted(d)
print("union is",d)


