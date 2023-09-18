String = "fedcba"
print('Original String: ', String)
lst = list(String)
lst.sort()
print('Sorted String: ')
for i in lst:
	print(i, end = "")
print(lst)
