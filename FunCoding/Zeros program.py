arr=eval(input())
z=[]
zeros=0
for i in range(len(arr)):
    if(arr[i]!=0):
        z.append(arr[i])
    else:
        zeros=zeros+1
while(zeros>0):
    z.append(0)
    zeros=zeros-1
print(z)


