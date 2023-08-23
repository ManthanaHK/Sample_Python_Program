# 1 Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
def ExchangeVariable(a:int,b:int):
    a,b = b,a
    return a,b

# 2 Python Program to Check Whether a Number is Positive or Negative
def PostiveOrNegative(num:int):
    if num<0:
        return True
    return False

# 3 Python Program to Print all Numbers in a Range Divisible by a Given Number
def RangeDivisible(size:int,num:int):
    divisible_list = []
    for i in range(size+1):
        if i%int(num) == 0:
            divisible_list.append(i)
    return divisible_list

# 4 Python Program to Read Two Numbers and Print Their Quotient and Remainder
def QuotientandRemainder(num1:int,num2:int):
    rem = num1%num2
    quo = int(num1/num2)
    return rem,quo

# 5 Python Program to Print Odd Numbers Within a Given Range
def listOfOddNumbers(size:int):
    odd_list = []
    for i in range(size):
        if i%2 != 0:
            odd_list.append(i)
    return odd_list

# 6 Python Program to Find the Sum of Digits in a Number
def SumOfDigits(digit:int):
    sum:int = 0
    while(digit!=0):
        rem = digit%10
        sum = sum + rem
        digit = digit//10
    return sum

# 7 Python Program to Find the Smallest Divisor of an Integer
def SmallestDivisor(num:int):
    min_divisor = []
    for i in range(2,num):
        if num%i == 0:
            min_divisor.append(i)
    small = min(min_divisor)
    return small

# 8 Python Program to Read a number n and Compute n+nn+nnn
def ProductandSum(num:int):
    sum:int = 0
    for i in range(1,num+1):
        iter = pow(num,i)
        sum = sum + iter
    return sum

# 9 Python Program to Reverse a Given Number
def ReverseNumber(num:int):
    reverse_number = 0
    while(num!=0):
        rem = num%10
        reverse_number =  reverse_number*10 + rem
        num = num//10
    return reverse_number

# 10 Python Program to Calculate the Average of Numbers in a Given List
def AverageOfList():
    num_list = [1,2,3,4,5,6,7]
    return sum(num_list)//len(num_list)

# 11 Python Program to Count the Number of Digits in a Number
def CountNumbers(digit:int):
    return len(str(digit))

# 12 Python Program to Check if a Number is a Palindrome
def CheckPalindrome(num:int):
    if ReverseNumber(num) == num:
        return True
    return False


# 13 Python Program to print the number of occurrence of a sub string in a given string
def count_substring_occurrences(main_string, sub_string):
    count = main_string.count(sub_string)
    return count

# 14 def lowest_index_of_substring(main_string, sub_string):
def lowest_index_of_substring(main_string, sub_string):
    index = main_string.find(sub_string)
    return index

# 15 Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False
def ChracterCheck(string:str):
    return string.isalpha()

# 16 Python Program to Replace all Occurrences of ‘a’ with $ in a String
def replaceAlphabet(string:str):
    return string.replace("a","$")

# 17 Python Program to Count the Number of Vowels in a String
def CountVowels(string:str):
    count:int = 0
    vowels_list = ['a','e','i','o','u']
    for i in string:
        if i in vowels_list:
            count = count + 1
    return count

# 18 Python Program to Take in a String and Replace Every Blank Space with Hyphen
def ReplaceWithHyphen(string:str):
    return string.replace(" ","-")

# 19 Python Program to find the length of string without using any built-in functions
def LengthOfString(string:str):
    cnt:int = 0
    for i in string:
        cnt = cnt + 1
    return cnt

# 20 Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
def LargerString(string1:str,string2:str):
    cnt1:int = 0
    cnt2:int = 0
    for i in string1:
        cnt1 = cnt1 + 1
    for i in string2:
        cnt2 = cnt2 + 1
    if(cnt1 > cnt2):
        return string1
    return string2

# 21 Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
def numberUpperSmaller(string:str):
    smallCnt:int = 0
    bigCnt:int = 0
    for i in string:
        if i.islower() == 1:
            smallCnt = smallCnt + 1
        elif i.isupper() == 1:
            bigCnt = bigCnt + 1
    return smallCnt,bigCnt

# 22 Python Program to Calculate the Number of Digits and Letters in a String
def digitCharacterCount(string:str):
    cntDigit:int = 0
    cntCharacter:int = 0
    for i in string:
        if i.isdecimal() == 1:
            cntDigit = cntDigit + 1
        if i.isalpha() == 1:
            cntCharacter = cntCharacter + 1
    return cntCharacter, cntDigit

# 23 Python Program to check whether a full pattern (not sub string) is present in the given sentence
def checkString(string:str):
    sentence = "Monday comes after sunday"
    if sentence.find(string) == -1:
        return 0
    else :
        return 1

# 24 Cumulative sum of a list [1, 2, 4, ...] is defined as[1, 3, 7, . . .]Write a functioncumulative_sum() to compute cumulative sum of a list
def sum_of_list():
    arr = [0,9,-1,2,-3]
    sum_array_list = []
    add = 0
    for i in range(len(arr)):
        add = add + arr[i]
        sum_array_list.append(add)
    return sum_array_list

# 25 Write a program to generate 10 random integers
import random

def random_generator():
    for i in range(10):
        print(random.randint(10,30))
# random_generator()

# 26 Write a program to generate 10 random integers between 1 to 20 (both inclusive)
def random_generator_between_1and20():
    for i in range(10):
        print(random.randint(1,20))
#random_generator_between_1and20()

# 27 Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique
def unique_randomGenerator():
    unique = []
    for i in range(10):
        rand = random.randint(1,20)
        if rand not in unique:
            print(rand)
            unique.append(rand)
#unique_randomGenerator()

# 28 Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc
def random_1to100():
    cnt1 = 1
    cnt2 = 2
    cnt3 = 3
    cnt4 = 4
    cnt5 = 5
    cnt6 = 6
    cnt7 = 7
    cnt8 = 8
    cnt9 = 9
    cnt10 = 10

    total = 0
    while(total<=10):
        rand = random.randint(1,100)
        if rand>=1 and rand<=10:
            if cnt1 == 1:
                print(rand)
                total = total + 1
                cnt1 = 0
        if rand>=11 and rand<=20:
            if cnt2 == 2:
                print(rand)
                total = total + 1
                cnt2 = 0
        if rand>=21 and rand<=30:
            if cnt3 == 3:
                print(rand)
                total = total + 1
                cnt3 = 0  
        if rand>=31 and rand<=40:
            if cnt4 == 4:
                print(rand)
                total = total + 1
                cnt4 = 0    
        if rand>=41 and rand<=50:
            if cnt5 == 5:
                print(rand)
                total = total + 1
                cnt5 = 0  
        if rand>=51 and rand<=60:
            if cnt6 == 6:
                print(rand)
                total = total + 1
                cnt6 = 0
        if rand>=61 and rand<=70:
            if cnt7 == 7:
                print(rand)
                total = total + 1
                cnt7 = 0
        if rand>=71 and rand<=80:
            if cnt8 == 8:
                print(rand)
                total = total + 1
                cnt8 = 0
        if rand>=81 and rand<=90:
            if cnt9 == 9:
                print(rand)
                total = total + 1
                cnt9 = 0
        if rand>=91 and rand<=100:
            if cnt10 == 10:
                print(rand)
                total = total + 1
                cnt10 = 0
        else:
            continue
# random_1to100()