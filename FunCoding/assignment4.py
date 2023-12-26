# program to find frequency of letters in string

a=str(input("enter a string:"))
count=0
for letter in a:
    print(letter,"-",a.count(letter))
