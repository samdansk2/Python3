arr=[2,3,4,6,5,1]
k=2
ab=[]
for i in range((len(arr)-k),len(arr)):
    ab.append(arr[i])
for i in range((len(arr)-k)):
    ab.append(arr[i])
print(ab)
