n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    for j in range(n-i-1):
        print(" ",end=" ")
    print()    

#list
lis=[]
lis.append(10)
print(lis)
for i in range(20,101,10):
    lis.append(i)
print(lis)
