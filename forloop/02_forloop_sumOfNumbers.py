initial = int(input("Enter the initial value : ")) # 1
final = int(input("Enter the final value : ")) # 100

sum = 0

for i in range(initial, final+1):
    sum = sum + i


print(f"The summation result between {initial}-{final} is : {sum}")
