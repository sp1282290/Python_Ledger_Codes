s1 = 'Python is a versatile programming language'
li=s1.split()
print(li)

s2='ABCD'
li=s2.split()
print(li)


new_str= ''.join(li)
print(new_str)

s2='ABCDert'
li=s2.split()
print(li)


new_str1= '-'.join(li)
print(new_str1)

s1 = '10 20 30 40 1'
print(s1.split()) #['10', '20', 30', '40']
li= ['Hello', 'World']
print(" ".join(li))# Hello World