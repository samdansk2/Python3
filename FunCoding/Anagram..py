a=str(input("enter a string:"))
b=str(input("enter a string:"))
count=0
count1=0
if(len(a)==len(b)):
    for i in range(len(a)):
        if(a[i] in b):
            count+=1
        if(b[i] in a):
            count1+=1
    if(count==count1):
        print("yes")
    else:
        print("no")
else:
    print("no")
