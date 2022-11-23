
a = [1,2,3]
b = a
b[0] = 11


b =a[:]
b[0] = 10

a=[1,2,3,4,5]

print(list(a))

a=[1,2,3,4,5]

print(a.copy())



from copy import deepcopy

l = [[1,2],[3,4]]

l2 = deepcopy(l)
print(l2)


