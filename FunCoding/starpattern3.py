n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


print()
print()

n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
            
