import os

i = 1
while i<=100:
    filename = "Files" + str(i) + ".c"
    # print(filename)
    f = open(os.path.join("logs",filename), "w")
    f.close()
    i += 1

print("100 log file created")