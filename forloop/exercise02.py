# program will ask you how many elements you want to add
# then it will ask you to enter the elements one by one
# then it will print the sum only even values
# recall : add value in list, list.append(6)

noValues = int(input("How many values you want to enter? : ")) # 5
l = []

for i in range(noValues):
    element = int(input(f"Enter number #{i+1} : "))
    l.append(element)

sum = 0
for x in l:
    if x%2 == 0:
        sum = sum + x

print("Sum of all evenvalues you have entered is :",sum)