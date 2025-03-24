li = []
# Adding element into list---->append(): it will add the element at the end of the list.Append does not return anything if u print it will give None
li.append(100)
li.append(20)
print(li)
# Inserting element with specific index usin insert():----->it will add the element at particular defind index like as li.index(index,element). It does not return anything
li.insert(0,500)
print(li)# [500,100,20]
# pop(): pop methods without any argument removes and returns last element from the list.
ele = li.pop()
print(ele)#20
print(li)#[500,100]

#pop(index): pop can removes specific index element from the list
print(li.pop(0))# 500
print(li)#100

li.append(700)#[100,700]
print(li)

#remove():remove element from list(Only first occurance)
li.remove(700)
print(li)#100
li.append(900) 
print (li)#[100,900]


# del Keyword:
del li[1]
print(li)# [100]

del li # deletes whole object from the memory.
#print(li)#Error
S="10 20 30 30 30  30  40  50 60"
b=S.split()
print("The array are: ",b,end=" ")

g=[10,20,20,30,20,40,50]
res=g.count(20)
print("the count is",res)
