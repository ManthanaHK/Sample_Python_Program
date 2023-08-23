# 1 Python Program to Find the Largest Number in a List
def largestNumber_list():
    array = [1,245,23,-9,0,89,455]
    return max(array)

# 2 Python Program to Find the Second Largest Number in a List
def secondLargestNumber():
    array = [1,245,23,-9,0,89,455]
    array.remove(max(array))
    return max(array)

# 3 Python Program to Put Even and Odd elements in a List into Two Different Lists
def oddEven_list():
    array = [0,-9,89,2,1,7,-89,78,12]
    odd_list = []
    even_list = []
    for i in array:
        if i == 0:
            continue
        elif i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return odd_list,even_list

# 4 Python Program to check whether two lists are same
def compareList():
    arr1 = [0,-89,7,1,2,0]
    arr2 = [0,-89,7,1,2,0]
    if arr1 == arr2:
        return 1
    return 0

# 5 Python Program to Find the Union of Lists
def unionList():
    arr1 = [0,89,2,2,1,-9]
    arr2 = [0,12,2,2,5,-9]
    union = []
    for i in arr1:
        if i not in union:
            union.append(i)
    for i in arr2:
        if i not in union:
            union.append(i)
    return union

# 6 Python Program to Find the Intersection of Lists
def intersectionList():
    arr1 = [0,-10,2,45,-10,13]
    arr2 = [0,-10,92,5,-10,13]
    intersection = []
    for i in arr1:
        if i in arr2:
            if i not in intersection:
                intersection.append(i)
    return intersection

# 7 Python Program to find union and intersection of lists without repetition

# 8 Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
def createTuple():
    square_tuple = ()
    for i in range(1,6):
        print(square_tuple.__add__((i,i*i)))
# createTuple()

# 9 Python Program to Remove the Duplicate Items from a List
def duplicateremoveList():
    arr = [1,3,5,7,3,-5,7,-7,-7]
    for i in range(len(arr)):
        cnt = 0
        if i < len(arr):
            ele = arr[i]
            for j in range(len(arr)):
                if arr[j] == ele:
                    cnt = cnt + 1
            if cnt != 0:
                arr.pop(i)
    return arr

# 10 Python Program to Read a List of Words and Return the Length of the Longest One
def longestWord():
    word1 = input("Enter first word:\n")
    word2 = input("Enter second word:\n")
    word3 = input("Enter third word:\n")
    if len(word1) > len(word2) and len(word1) > len(word2):
        print(len(word1))
    elif len(word2) > len(word1) and len(word2) > len(word3):
        print(len(word2))
    else:
        print(len(word3))
# longestWord()

# 1 Python Program to Add a Key-Value Pair to the Dictionary
def addToDictionary():
    dictionary = {1:"A",2:"B",3:"C"}
    dictionary[4] = "D"
    return dictionary

# 2 Python Program to Concatenate Two Dictionaries Into One
def ConcatenateDictionary():
    dic1 = {1:"A",2:"B"}
    dic2 = {1:"C",2:"D"}

    second_dict = {**dic1, **dic2}
    concatenated_dict = {}

    for key, value in dic1.items():
        concatenated_dict[key] = value

    for key, value in dic2.items():
        if key not in concatenated_dict:
            concatenated_dict[key] = value

    print(concatenated_dict)
    print(second_dict)
# ConcatenateDictionary()

# 3 Python Program to Check if a Given Key Exists in a Dictionary or Not
def checkKey(key):
    dic1 = {1:"A",2:"B"}
    if key in dic1.keys():
        return 1
    return 0

# 4 Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x)
def createDictionary_n(n):
    dic_n = {}
    for i in range(1,n+1):
        dic_n[i] = i*i
    print(dic_n)
# createDictionary_n(3)

# 5 Python Program to Sum All the Items in a Dictionary
def sumOfDictionary():
    dic = {"A":1,"B":2}
    print(sum((dic.values())))
# sumOfDictionary()

# 6 Python Program to Multiply All the Items in a Dictionary
def multilplyItem():
    dic = {"A":1,"V":3,"C":4}
    pro = 1
    for i in dic.values():
        pro = pro * i
    print(pro)
# multilplyItem()

# 7 Python Program to Remove the Given Key from a Dictionary
def removekey(key):
    dic = {"A":1,"B":3}
    dic.pop(key)
    print(dic)
# removekey("A")

# 8 Write a function is_empty(my_dict) that takes a dictionary my_dict and returns True if my_dict is empty and False otherwise
dic1 = {}
def my_dict(dictionary:dict):
    if len(dictionary.keys()) == 0:
        return True
    return False

# 9 Write a function make_dict(key_value_list) that takes a list of tuples key_value_list 
# where each tuple is of the form (key, value) and returns a dictionary with these keys and corresponding values 
def make_dict(t1:tuple, t2:tuple):
    created_dict = {}
    list_tuples = []
    list_tuples.append(t1)
    list_tuples.append(t2)
    for i in list_tuples:
        for j in range(len(i)):
            created_dict[i[j]] = i[j+1]
            break
    print(created_dict)
# make_dict((1,"A"),(2,"B"))


# 10 simple  substitution  cipher  is  an  encryption  scheme
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w',
               'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o',
               'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 
               'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 
               'n': 'a', 't': ' ', 'w': 't'
            }
def encrypt(phrase,cipher_dict):
    encrypted_phrase = ''
    for i in phrase:
        encrypted_phrase = encrypted_phrase + cipher_dict[i]
    print("The envcrypted phrase is {}".format(encrypted_phrase))
# encrypt("cat", CIPHER_DICT)

# 11 Write a function make_cipher_dict(alphabet) that takes a string of unique characters and returns a randomly-generated cipher 
# dictionary for the characters in alphabet . You should use the shuffle() method in the random module to ensure that your returned 
# cipher dictionary is random
import random
def make_cipher_dict(string):
    createdDict = {}
    val = []
    for i in CIPHER_DICT.values():
        val.append(i)
    for i in range(len(string)):
        random.shuffle(val)
        createdDict[string[i]] = val[i]
    print(createdDict)
# make_cipher_dict('alpha')

# 12 Write a python code to generate grade using dictionary. Dictionary should have student names as keys (assuming names are unique) 
# and subject_name and mark as value. There are 5 subjects for each student. Marks should be converted to grades (90 –100 A+, 80-89 A etc)
studentDetails = {
    "Amar" : {"Maths":95,"Biology":85,"Physics":75,"Chemistry":65,"Social Sceince":67},
    "Adhamya" : {"Maths":90,"Biology":80,"Physics":70,"Chemistry":63,"Social Sceince":61}
}

def gradeCoverter(marks):
    if marks>90:
        return "A"
    elif marks>80 and marks<=90:
        return "B"
    elif marks>70 and marks<=80:
        return "C"
    elif marks>60 and marks<=70:
        return "D"
    else:
        return "E"

def studentGrade(details):
    for key,value in details.items():
        print(f"The student is: {key}")
        for sub,marks in value.items():
            print(f"{sub}: Grade is {gradeCoverter(marks)}")
        print("\n")

studentGrade(studentDetails)