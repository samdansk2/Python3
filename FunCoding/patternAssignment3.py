n=3
for i in range(n):
    for j in range(n):
        if(i+j==i):
            print("A",end="")
        if(i==1 and i+j==2):
            print("B",end="")
        if(i==2 and i+j==3):
            print("B",end="")
        if(i+j==4):
            print("C",end="")
        else:
            print("",end="")
    print()
print()#This print is for space only in output interface

n=int(input("enter the number:"))
alpha=65
for i in range(n+1):
    for j in range(i):
        print(chr(alpha+j),end=" ")
    print()
