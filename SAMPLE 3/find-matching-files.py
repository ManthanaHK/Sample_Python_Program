import os, sys

def findMatchinfFiles(folderPath):
    fileList = []
    repeatedList = []
    lst = os.listdir(folderPath)
    for i in lst:
        if os.path.isfile(folderPath+"\\"+i):
            if i in fileList:
                i.append(repeatedList)
    print(repeatedList)

if len(sys.argv) != 2:
    print("USAGE: python <python file> <folder path>")
else:
    path = sys.argv[1]
    findMatchinfFiles(path)