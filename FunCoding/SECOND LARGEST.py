def Secmax(arr):
    arr.sort()
    ele={"max":arr[-2]}
    return ele
arr=eval(input())
kn=Secmax(arr)
print(kn["max"])
