n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if(i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
