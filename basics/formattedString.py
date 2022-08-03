number1 = input("Enter the first number : ")
number2 = input("Enter the second number : ")

ans = int(number1) + int(number2)

# way 1 --> comma method
print("The answer is",ans)

# way 2 --> format method
print("The answer is {ans}".format( ans = ans ))

# way 3 --> f method
print(f"The answer is {ans}")
