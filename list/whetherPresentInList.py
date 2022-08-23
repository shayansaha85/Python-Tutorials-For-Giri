"""
n = 4
l = [3,5,4,6,7]

"""
n = 99
l = [3,5,4,6,7]
count = 0

i = 0

while i<len(l):
    if n == l[i]:
        count = count+1
    i += 1

if count == 0:
    print(f"{n} is not present in {l}")
else:
    print(f"{n} is present in {l}")
