name = input("Enter your name : ")
areYouAnIndian = input("If Indian type 'y/Y' or type 'n/N : ")

if areYouAnIndian == 'y' or areYouAnIndian == 'Y':
    age = int(input("Enter your age : "))
    if age >= 18:
        print(f"{name}, you are Indian and you are above 18. You are eligible")
    else:
        print(f"{name}, you are still minor, hence not eligible")

else:
    print(f"{name}, you are not Indian, hence not eligible for vote")