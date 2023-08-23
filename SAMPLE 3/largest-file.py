import os,sys

def largestFile(folderPath):
    fileSize = {}
    files = os.listdir(folderPath)
    for file in files:
        size = os.path.getsize(folderPath+"\\"+file)//1024
        fileSize[size] = folderPath+"\\"+file
    largeSize = max(fileSize.keys())
    print(f"The largest file is {fileSize[largeSize]} and is {largeSize} KB.")


if len(sys.argv) != 2:
    print("USAGE: pyton <python file> <direcctory path>")
else:
    path = sys.argv[1]
    largestFile(path)