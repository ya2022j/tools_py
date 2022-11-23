

lst = [2,3,4]

def minIndex(lst):
    return min(range(len(lst)),key=lst.__getitem__)


def maxIndex(lst):
    return max(range(len(lst)),key=lst.__getitem__)



print(minIndex(lst))
print(maxIndex(lst))