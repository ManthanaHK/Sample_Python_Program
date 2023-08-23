def fileCharacter(filename = input("Enter file path: ")):
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        print(f"Total Lines: {num_lines}\nTotal Words:{num_words}\nTotal Chars:{num_chars}")
    except FileNotFoundError:
        print("File not found")

fileCharacter()