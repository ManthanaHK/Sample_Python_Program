import sys

def sumOfFile(filename):
    try:
        with open(filename,'r') as file:
            content = file.read()
            lines_list = content.split("\n")
            sum = 0
            for line in lines_list:
                for charac in line:
                    if ord(charac) >=47 and ord(charac) <= 59:
                        sum = sum + int(charac)
            print(sum)
    except FileNotFoundError:
        print("File Not Found")

# if len(sys.argv) != 2:
#     print("Enter: python <python_file> <filename>")
# else:
#     file = sys.argv[1]
#     sumOfFile(file)
sumOfFile("E:\\ADS LabFiles\\SAMPLE 3\\Dummy File 2.txt")