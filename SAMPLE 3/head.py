import sys

def print5Lines(filename):
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            count = 0
            for i in lines:
                for j in i.split("."):
                    if (count <= 5):
                        print(j)
                        count = count + 1
    except FileNotFoundError:
        print("File not found")

if len(sys.argv) != 2:
    print("ENTER: python head.py <filename>")
else:
    filename = sys.argv[1]
    print5Lines(filename)