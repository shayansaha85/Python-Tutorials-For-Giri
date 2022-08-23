
n = int(input("Enter a number = "))
sum = 0
while n != 0:
    remainder = n%10
    sum = sum + remainder
    n = n//10

print("The sum of all digits :", sum)

"""
# iteration 1
remainder = 1
sum = 1
n = 89

# iteration 2
remainder = 9
sum = 10
n = 8

# iteration 3
remainder = 8
sum = 18
n = 0


"""