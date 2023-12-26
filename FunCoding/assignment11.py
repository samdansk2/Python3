# longest sequence of consecutive one's 
arr=eval(input())
count=0
maxi=0
for i in arr:
    if(i==1):
        count+=1
        maxi=max(maxi,count)
    else:
        count=0
print("Number of consecutive 1's are:",maxi)
