n=int(input("enter a number:"))
string=str(n)
b=len(string)
sum = 0
temp = n
while temp > 0:
    digit=temp % 10
    sum += digit**b
    temp//=10
if(n==sum):
    print("Yes")
else:
    print("No")
