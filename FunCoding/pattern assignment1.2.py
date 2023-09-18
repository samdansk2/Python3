n=int(input("enter a number:"))
for i in range(n):
    for j in range(n+i-n):
        print(" ",end=" ")
    for j in range(n-2*i+n-1):
        print("*",end=" ")
    for j in range(n+i-n):
        print(" ",end=" ")
    print()
        
