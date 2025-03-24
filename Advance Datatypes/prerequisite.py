s1 = "This is a test. This test is simple."
s1 = s1.replace('.'," ")
print(s1)
print(s1.count('This'))# 2
print(s1.count('is'))#4 
# due to is coming two time and it shows 4 because it count the sub part of word i.e we need to use another way
print(s1.count('a'))#1
print(s1.count('test'))#2
print(s1.count('This'))#2
print(s1.count('test'))#2
print(s1.count('is'))#4
print(s1.count('simple'))#1