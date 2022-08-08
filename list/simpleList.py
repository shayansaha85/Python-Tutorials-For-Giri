l = [44,35,6,74,8,11,72]

print(type(l))

# methods are almost same like String

# indexing
firstEl = l[0]
print("First element",firstEl)

# length
length = len(l)
print("Length",length)

# slicing
fetchFirst5 = l[0:5]
print(fetchFirst5)

# sort - ascending
l.sort()
print(l)

# sort - descending
l.sort(reverse=True)
print(l)

# adding elements
l1 = [1,2,3,4,5]
l1.append(6)
print(l1)

# insert
l1.insert(0, 17)
print(l1)

# remove
l2 = [5,4,3,1,6]
l2.pop(0)
print(l2)