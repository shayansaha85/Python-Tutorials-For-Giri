oddCount = 0

n = int(input("Enter a number : ")) # 348
while n!=0:
    remainder = n%10 
    
    if remainder%2 != 0:
        oddCount = oddCount+1

    n = n//10

print(f"There are {oddCount} odd digit in the number")