"""
WAP in python to find the count of even numbers in a input

example:

input : 348
output : 2

input : 319
output : 0

"""


evenCount = 0

n = int(input("Enter a number : ")) # 348
while n!=0:
    remainder = n%10 
    
    if remainder%2 == 0:
        evenCount = evenCount+1

    n = n//10

print(f"There are {evenCount} even digit in the number")