 #TODO: Prompt the user to enter a number and store it in num
num = int(input("Enter a number: "))
# TODO: Initialize a variable to keep track of the sum of the digits
sum = 0
# TODO: Use a while loop to iterate and calculate the sum of the digits
while (num > 0):
    digit = num % 10
    sum = sum + digit
    num //= 10 # Remove the last digit
# TODO: Print the sum of the digits
print("The sum of the digits is",sum)