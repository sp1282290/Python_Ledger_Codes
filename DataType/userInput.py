s1 ='    Code    '
print(s1.strip())
s2= '--Code--'
print(s2.strip('-'))
print(s2.lstrip('-'))
print(s2.rstrip('-'))

# TAKING INPUT FROM USER
num1=input()# by default it will take string
num2=input()# by default it will take string
print(f'Adiition of {num1} and {num2} is: {num1+num2}')

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(f'Adiition of {num1} and {num2} is: {num1+num2}')

#WAC to accept string value from user and store it into s1 by removing
#leading and trailing spaces.

s1 = input().strip()
print(s1)

s2= 'Code with Me..!!'
print(s2.find('with'))