n=int(input("enter no. of elements you want to enter"))
lis=[]
for i in range(n):
      element=int(input("enter the element"))
      lis.append(element)
print(lis)

product=1
for i in lis:
    product*=i
print("product=",product)
    
    
