def sam(arr):
    maxi=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
    return(maxi)
arr1=eval(input())
arr2=eval(input())
s1max=sam(arr1)
s2max=sam(arr2)
print(s1max)
print(s2max)
if(s1max>s2max):
    print(s1max-s2max)
else:
    print(s2max-s1max)
