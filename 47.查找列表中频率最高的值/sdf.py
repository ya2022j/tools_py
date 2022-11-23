

a = [1,2,3,4,54,5,6,67,6,6,6,2]


print(max(set(a),key=a.count))


from collections import Counter


cnt = Counter(a)

print(cnt.most_common(3))