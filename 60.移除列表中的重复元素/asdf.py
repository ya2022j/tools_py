


items = [1,2,3,4,4,4]
newitems2  = list(set(items))

print(newitems2)


from collections import OrderedDict

items = ["foo","bar","bar","foo"]
print(list(OrderedDict.fromkeys(items).keys()))