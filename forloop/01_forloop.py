# 1 to 10


# for i in range(0,11,2):
#     print(i)

# for j in range(10,0, -1):
#     print(j)

# replace all the numbers with a variable --> "i"
# range | in python upper limits always excluded

# find the sum of all numbers between 1 to 100
sum = 0 # if we are doing - or +
# we will initiate with 1 if *
mult = 1

for i in range(1,101):
    sum = sum + i
    mult = mult*i

print("the summation of all the numbers is :",sum)
print("the multiplication of all the numbers is :",mult)
