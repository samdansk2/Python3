arr=[1,2,1,1,1,1,4,5,1,1,1]
count=0
maxi=0
for i in range(len(arr)):
    if (arr[i]==1):
        count+=1
    else:
        count=0
    maxi=max(maxi,count)
print(maxi)
