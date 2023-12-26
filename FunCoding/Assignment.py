# Program to find longest consecutive sequence of numbers
# Example:
# Input: lis = [100, 101, 102, 103, 2, 3, 9]
# Output: 4  

maxi=0
lis=[100,101,102,103,2,3,9]
for i in lis:
    current=i
    count=0
    while(current in lis):
        count=count+1
        current=current+1
        maxi=max(maxi,count)
print(maxi)
