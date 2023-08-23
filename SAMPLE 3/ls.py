import os,sys

def listFiles(filePath):
    files = os.listdir(filePath)
    for i in files:
        print(str(i)+"\n")

if len(sys.argv) == 2:
    enteredPath = sys.argv[1]
    listFiles(enteredPath)
elif len(sys.argv) == 1:
    enteredPath = "E:\\ADS LabFiles"
    listFiles(enteredPath)
else:
    print("USAGE: python <python file> <directory path>")
