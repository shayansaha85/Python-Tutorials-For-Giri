import os

def isLog(filename):
    l = filename.split(".")
    extension = l[-1]
    if extension == "log" or extension == "LOG":
        return True
    else:
        return False

def removeLogFiles(foldername):
    files = os.listdir(foldername)

    for x in files:
        if isLog(x):
            os.remove(os.path.join(foldername, x))

removeLogFiles("logs")

