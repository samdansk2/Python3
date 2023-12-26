# program to find lower and upper case letters in string
 
a=str(input("enter a string:"))
upper=""
for char in a:
    if char.isupper():
        upper+=char
print(upper,end=" ")
lower=""
for char in a:
    if char.islower():
        lower+=char
print(lower)

