import sys, os

def findingFiles(folderPath):
    file_list = [file for file in os.listdir(folderPath) if os.path.isfile(folderPath+"\\"+file)]
    print(file_list)

if len(sys.argv) != 2:
    print("USAGE: python <python file> <folder path>")
else:
    path = sys.argv[1]
    findingFiles(path)