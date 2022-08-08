
# li = [5,4,3,2,3,3,5,6,7,8,9,9,9,0,1,2,3,1,1]
# find the count of distinct elements

# step 1 : find another list with only distinct elements
li = [5,4,3,2,3,3,5,6,7,8,9,9,9,0,1,2,3,1,1]
li2se = set(li)
# li2se is a set NOT LIST
distinctList = list(li2se)
print(distinctList)

# step 2 : find the length of that list
print("Distinct element count :", len(distinctList))