import sys

def copyingFiles(filename1, filename2):
    try:
        with open(filename1,'r') as source_file, open(filename2,'a') as destination_file:
            content = source_file.read()
            destination_file.write(content)
            print("Succesfully Appended")
    except FileNotFoundError:
        print(f"Mistake in file path")

if len(sys.argv) != 3:
    print("ENTER: pyhton <python_file> <source_file> <destination_file>")
else:
    src = sys.argv[1]
    dst = sys.argv[2]
    copyingFiles(src,dst)