def sam(arr):
    maxi=0
    for i in range(len(arr)):
        maxi=max(maxi,arr[i])
    return(maxi)
arr1=eval(input())
arr2=eval(input())
arr1=[abs(i) for i in arr1]
arr2=[abs(i) for i in arr2]
s1max=sam(arr1)
s2max=sam(arr2)
print(s1max)
print(s2max)
if(s1max>s2max):
    print(s1max-s2max)
else:
    print(s2max-s1max)

#two problems eixst in this

#1 is max element finding(from 2nd line to 4th line)

#another one is function max of two arrays
