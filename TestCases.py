from sample1 import *
from sample2 import *
from sample3 import *

# Sample 1

assert ExchangeVariable(-9,0) == (0,-9)

assert PostiveOrNegative(-2) == True

assert RangeDivisible(20,4) == [0,4,8,12,16,20]

assert QuotientandRemainder(5,3) == (2,1)

assert listOfOddNumbers(10) == [1,3,5,7,9]

assert SumOfDigits(10) == 1

assert SmallestDivisor(32) == 2

assert ProductandSum(3) == 39

assert ReverseNumber(12345) == 54321

assert AverageOfList() == 4

assert CountNumbers(1234) == 4

assert CheckPalindrome(121) == True

assert count_substring_occurrences("Politics is corrupt","corrupt") == 1

assert lowest_index_of_substring("ABCDijkLMNOPijk","ijk") == 4

assert ChracterCheck("Manthan") == True

assert replaceAlphabet("Manthana") == "M$nth$n$"

assert CountVowels("Audio") == 3

assert ReplaceWithHyphen("Manthana is in MSIS") == "Manthana-is-in-MSIS"

assert LengthOfString("Manthana") == 8

assert LargerString("Manthan","Girl") == "Manthan"

assert numberUpperSmaller("ManaTHANA") == (3,6)

assert digitCharacterCount("Man10@200Agam") == (7,5)

assert checkString("comes") == 1

assert sum_of_list() == [0,9,8,10,7]

# Sample 2

assert largestNumber_list() == 455

assert secondLargestNumber() == 245

assert oddEven_list() == ([-9,89,1,7,-89],[2,78,12])

assert compareList() == 1

assert unionList() == [0,89,2,1,-9,12,5]

assert intersectionList() == [0, -10, 13]

assert duplicateremoveList() == [3,7,-5,-7]

assert longestWord() == 9

assert addToDictionary() == ({1: 'A', 2: 'B', 3: 'C', 4: 'D'})

assert checkKey(1) == 1

assert my_dict(dic1) == True

# Sample 3

assert unique() == ([5,7])

assert dupElements() == [12,3,4]