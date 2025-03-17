# String to int conversion:
'''
In Python while converting string to int , only when string is holding int value to int conversion is allowed
'''
print(int('12'))#12
# print(int('code')) # error
# print(int('12.44'))# error
# print(int('True'))# error
# WAC to take 2 float numbers from user and display its addition
a=(float(input("Enter a float number 1:")))
b=(float(input("Enter a float number 2:")))
c=a+b
print("The result of sum is",c)
#ROUND OF THE NUMBER USING TWO WAYS
print(round(4353454.3434,2))#4353454.34
print('{:.2f}'.format(45.34543))#45.35