lis=[3,3,2]
maxi=0
ab=-2000000
for i in range(len(lis)):
    temp=lis.count(lis[i])
    if(temp>maxi):
        maxi= temp
        ab=i
print("Most frequent element is:",lis[ab])


