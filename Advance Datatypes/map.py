li=[1,2,3,4]

def square(ele):
  return ele * ele
# map(function,iterable object)
result=map(square,li)
print(result) # <map object at 0x1009d7130>
print(list(result))

li2 = ['10','20','30','40','50']
print(li2)# ['10','20','30','40','50']
new_li=list(map(int,li2))
print(new_li)#[10 20 30 40 50]
li3=[1,2,3,0]
print(li3)
print(list(map(float,li3))) #[1.0,2.0,3.0,4.0]
print(list(map (bool,li3))) #[True,True,True,False]