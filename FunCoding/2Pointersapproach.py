s=str(input("enter a string:"))
flag=0
pointer1=0
pointer2=len(s)-1
while(pointer1<pointer2):
    if(s[pointer1]!=s[pointer2]):
        flag=1
        break
    pointer1+=1
    pointer2-=1
if(flag==0):
    print("palindrome")
else:
    print("no")
