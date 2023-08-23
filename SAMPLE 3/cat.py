import sys

def cat(fileName):
    try:
        with open(fileName,'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"{fileName} Not Found") 

if len(sys.argv) != 2:
    print(f"Enter: python cat.py <filename>")
else:
    entredFile = sys.argv[1]
    cat(entredFile)