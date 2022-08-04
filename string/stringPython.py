name = "Giridharan"
print(type(name))

# length of the string
# same for all datastructure except numeric values : int, float

length = len(name)
print(length)

# indexes
"""
G i r i d h a r a n
0 1 2 3 4 5 6 7 8 9
"""

firstLetter = name[0]
lastLetter = name[-1]

print("Last letter:",lastLetter)

# slicing of string***
"""
G i r i d h a r a n
0 1 2 3 4 5 6 7 8 9
"""
substring = name[2:7]
print(substring)

lastval = name[4:]
print(lastval)

firstval = name[:4]
print(firstval)

# reverse
reverseOfString = name[::-1]
print(reverseOfString)

# cases -> upper case and lower case
print(name.upper())
print(name.lower())

# split
maxvalue = "-maxSizeLimit=34"
l = maxvalue.split("=")
print(l)

fullname = "Shayan Saha"
separatefnamelname = fullname.split()
print(separatefnamelname)

# replace
s = "Flowar"
correctSpell = s.replace("a", "e")
print(correctSpell)

removeW = s.replace("w", "")
print(removeW)


# trailing spaces
username = " giridharan.s"
print(len(username))

usernameRemoveSpaces = username.strip()
print(len(usernameRemoveSpaces))

# ascii value
alph = 'a'
print(ord(alph))

