# python program to find palindrome of given string

x =str(input("enter a string:"))
w = ""
for i in x:
	w = i + w
if (x == w):
        print("Yes")
else:
        print("No")
