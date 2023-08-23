import sys

def patternRecognition(filename, pattern):
    try:
        with open(filename,'r') as file:
            content = file.read()
            lines = content.split(".")
            for i in lines:
                if i.find(pattern) != -1:
                    print(i)
    except FileNotFoundError:
        print("File not found")

if len(sys.argv) != 3:
    print("ENTER: python grep.py <filepath> <pattern>")
else:
    file = sys.argv[1]
    searchPattern = sys.argv[2]
    patternRecognition(file, searchPattern)