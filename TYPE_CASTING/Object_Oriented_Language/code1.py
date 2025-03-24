class Employee:
  name='Priya'
  age = 33
  
  def teach(self):
    print("Employee is teaching")
e1 = Employee()
e2 = Employee()
print(e1.name)
print(e2.name)
e1.teach()
e2.teach()
'''
    1. The method which are present inside the class are called as Instance(Object) variable.
    2. For Instance Methods self parameter is must.
'''