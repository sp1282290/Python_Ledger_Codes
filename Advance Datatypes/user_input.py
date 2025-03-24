userData = input('Enter list elements seprated by space')# '10 20 30 40'
li=userData.split()
print(li)#['10,'20,30,'40']
# print('Code-with-priya'.split('-'))\
  
newli = []
for i in li:
    newli.append(int(i)) 
    
print("The average of numli are: ",sum(newli)/len(newli))
  