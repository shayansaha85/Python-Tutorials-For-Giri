"""
WAP in Python to find the count of digits?

Example:

input : 345
output : 3

count = 0
n = 345
remainder with 10 [n%10] ==> 5
count++ --> 1

n = n//10 --> n=34
reaminder ==> 4
count++ --> 2

n = n//10 --> n=3
remainder ==> 3
count++ --> 3

n = n//10 --> n=0
remainder ==> 0
count++ --> 4


"""
345


count = 0 # where we will store the total count of digits in the input
n = int(input("Enter a number : "))
while n!=0:
    remainder = n%10 
    count = count + 1
    n = n//10

print("Total count of digits =",count)























