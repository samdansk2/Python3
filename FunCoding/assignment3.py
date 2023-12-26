#python program to find odd numbers in given range
a=int(input("enter a low range:"))
b=int(input("enter a upper range:"))
for i in range(a+1,b+1):
    if(i%2==0):
        continue
    else:
        print(i)
    
