# most frequent character in the string 

str = input("enter a string:")
maxi = 0
most_char = str[0]

for char in str:
    temp = str.count(char)
    if temp > maxi:
        maxi = temp
        most_char = char

print("Most frequent character is:", most_char)


