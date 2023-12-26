# Given an array of N integers. Each packet can have a number of chocolates. 
# There are m students, the task is to distribute chocolate packets such that :
# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates 
# and the packet with minimum chocolates given to the students is "minimum". 

def choco(arr,n,m):
    if(m==0 or n==0):
        return 0
    arr.sort()

    if(n<m):
        return -1

    min_diff = arr[n-1] - arr[0]

    for i in range(len(arr)-m+1):
        min_diff=min(min_diff,arr[i+m-1]-arr[i])

    return min_diff

arr=[1,3,4,7,9,9,12,56]
m=5
n=len(arr)
print("min difference -",choco(arr,n,m))