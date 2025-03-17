#bool():
print(bool(12))# True
print(bool(12.456))#True
print(bool('code'))#True
print(bool(''))#False
print(bool(0))#False

#float():
print(float(123)) # 123.0
#print(float('code'))#Error
print(float('13.23'))#123.23
print(float(True))#1.0
print(float(False))#0.0

#int();
print(int(123.45))#123
print(int('123'))#123
print(int(True))#1
print(int(False))#0
#print(int('code'))#Error
#print(int('123.45'))#Error
'''
int('123.45')----Not Allowed
int(123.54)----Allowed
'''