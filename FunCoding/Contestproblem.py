n=int(input("enter a number:"))
for i in range(n):
    for j in range(2*n-1):
        if(i==n-1 or j==0 or j==2*n-2):
            print("4", end=" ")
        else:
            print(" ",end=" ")
    print()
