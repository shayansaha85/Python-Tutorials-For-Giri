vowels = ['a', 'e', 'i', 'o', 'u']

name = "giridhAran"
i = 0
length = len(name)
consoCount = 0

while i<10:
    if name[i].lower() not in vowels:
        consoCount = consoCount + 1
    i = i+1

print(consoCount)