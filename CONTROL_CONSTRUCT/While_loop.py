#WAC TO  PRINT 1-10 
# i=1
# while(i<11):
#   print(i)
#   i=i+1
# print("------")  
  
#WAC TO PRINT 1-5 BUT IF 3 DONT PRINT IT
for j in range(1,6):
  if(j==3):
    continue
  else:
    print(j)
print("------")     
#WAC TP PRINT 1-15 BUT IF NUMBER IS EQAUL TO 7 THE BREAK THE LOOP 
for k in range(1,16,1):
  if(k==7):
    break
  else:
    print(k)
    
#WAC TO PRINT THE table of given number by user in one line by space
num =int(input("Enter the number to print the table: "))
for i in range(1,11,1):
  print(i*num, end=" ")