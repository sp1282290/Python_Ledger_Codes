# WAC FOR CALCULATOR
num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))
choice = input("Enter Choice :Add-1, Sub-2, Mul-3,Div-4,SquareOfNumber-5,FloorDivision-6, Modulus-7 ")
if choice =='3':
  print("Multiplication is : ",num1 * num2)
elif choice =='2':
  print("Subtraction is : ",num1 - num2)
elif choice =='4':
  print("Division is : ",num1 / num2)
elif choice =='1':
  print("Addition is : ",num1 + num2)
elif choice =='5':
  print("Square of num1",num1 ** 2) 
  print("Square of num2: ",num2 ** 2)
elif choice == '6':
  print("Floor division :",num1 // num2)
elif choice == '7':
  print("Remainder is :",num1 % num2)
else:
  print("Invalid Choice...!!")