# FIND THE FIRST NON-REPEATING CHARACTER
from collections import Counter
s = "swiss"
count = Counter(s)
result = next((char for char in s if count[char] ==1),None)
print(result)# w------> is output

# REVERSE THE STRING
S1="CodeInQueries"
reversed_str = S1[::-1]
print(reversed_str)# seireuQnIedoC------>is output

#CHECK IF A STRING IS PALINDROME
S2="madam"
print(S2 ==S2[::-1])# True-------> is output

# REMOVE DUPLICATES FROM A STRING
S3= "Banana"
result="".join(dict.fromkeys(S3))
print(result)# Ban-------->is a output
