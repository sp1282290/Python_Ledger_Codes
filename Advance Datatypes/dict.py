d1 = {'name':'Priya',
      'age':33,
      'phone': 34568,
      'Maths':90,
      'Science':90,
      'name':'Ankit'
       }

print(d1,type(d1))

#Accessing dict value:
print(d1['name']) #Ankit
print(d1['Maths'])# 90

for i in d1:
  print(i)
print()
  
print("------")

for i in d1.keys():
  print(i, end="-")
print()
'''name-ageA'''
print("--------")

for i in d1.values():
  print(i, end="-")
print()  
print("--------")
for i in d1.items():
  print(i)
  