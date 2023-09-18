n=int(input("enter a number:"))
for i in range(n):
    for j in range(n+i-n):
        print(" ",end=" ")
    for j in range(n-2*i+n-1):
        print("*",end=" ")
    for j in range(n+i-n):
        print(" ",end=" ")
    print()


#tracing

n=3
foriinrange(3)#
#left spaces:
#for j in range(3+o-3)# 3+0-3=0
#print(space)0 spaces
#for j in range(3+1-3)# 3+1-3=1
#print(space)1  space
#for j in range(3+2-3)# 3+2-3=2
#print(space)2  space

#for stars:
#for j in range(3-2*0+2)# 3-0+2=5 
#print(star)# 5stars
#for j in range(3-2*1+2)#3-2+2=3
#print(star)# 3stars
#for j in range(3-2*2+2)#3-4+2=1
#print(star)# 1star

#right spaces:
#for j in range(3+o-3)# 3+0-3=0
#print(space)0 spaces
#for j in range(3+1-3)# 3+1-3=1
#print(space)1 space
#for j in range(3+2-3)# 3+2-3=2
#print(space)2 space

#left spaces + stars + right spaces = Given Pattern

