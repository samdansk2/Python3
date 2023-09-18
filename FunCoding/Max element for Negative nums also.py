n=eval(input())
maxi=n[0]
for i in range(1,len(n)):
    if (n[i]>maxi):
        maxi=n[i]
print(maxi)
