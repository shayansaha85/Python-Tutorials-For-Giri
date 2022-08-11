# n = 5
# for loop range --> 1 to n+1
# ans = 1*2*3*4*5

n = int(input("Enter a number : "))

ans = 1

for i in range(1, n+1):
    ans = ans*i

print(f"Factorial of {n} is : {ans}")