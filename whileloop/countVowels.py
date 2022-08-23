"""

name = "giridharan"
output = 4

1. create a list with vowels
2. iterate through the name and check whether the alphabet is present in the vowels list
"""

vowels = ['a', 'e', 'i', 'o', 'u']

name = "giridhAran"
i = 0
length = len(name)
vowelsCount = 0

while i<10:
    if name[i].lower() in vowels:
        vowelsCount = vowelsCount + 1
    i = i+1

print(vowelsCount)
