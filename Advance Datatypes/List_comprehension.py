#WAP to create new list of square of each element of li list.
li= [10,20,30,40]
sq=[]
for i in li:
  sq.append(i**2)
print('square lis is : ',sq)  

print( [i**2 for i in li])

# WAP to add +5 to each element of li and create new list of it.
print([i+5 for i in li])
# WAP to print list of even element from li1:
li1=[1,2,3,4,5,6,7,8,9]
print([i for i in li1 if i%2 == 0])