n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if(i>=j):
            print(j+1,end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if(j+i>=n-1):
            print(n-j,end=" ")
        else:
            print(" ",end=" ")
    print()
