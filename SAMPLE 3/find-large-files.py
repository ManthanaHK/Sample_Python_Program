# 12. Write a program find-large-files.py to find files recursively in a directory tree that are  larger  than  given  size.  
# The  program  should  accept  the  directory  and  the  size  as command-line argument. 
# The size can be also be specified with K, M and G suffix for KB, MB and GB respectively.

import os, sys

def largeFiles(folderPath, size):
    sz, format = size.split()
    files = os.listdir(folderPath)
    for file in files:
        if format == "KB":
            if os.path.getsize(folderPath+"\\"+file)//1024 > int(sz):
                print(f"The file is: {file}")
        if format == "MB":
            if os.path.getsize(folderPath+"\\"+file)//2048 > int(sz):
                print(f"The file is: {file}")

if len(sys.argv) != 3:
    print("USAGE: python <python file> <folder path> <size sizeformat>")
else:
    path = sys.argv[1]
    size = sys.argv[2]
    largeFiles(path,size)
