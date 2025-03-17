s1="Shivam"
print(s1[0])
print(s1[1])
print(s1[2])
print(s1[3])
print(s1[4])

print("The length of s1 is:",len(s1))
print("The access of last letter of s1",s1[-1])

# Creating sub string from main string:
s2 = "kodnest"
sub_string =s2[0:3]# Slicing of String
print(sub_string) #kod
print(s2)#kodnest
s3='code'
s4=s3.upper()
#String are immutable in Python
#Once we declear a string we cannot modify
# if you want to print the new string oject refrence variable must be created
print(s3) #code
print(s4)