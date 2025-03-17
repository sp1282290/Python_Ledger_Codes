# TODO: Prompt the user to enter a number and store it in num
num=int(input("Enter a number"))
# TODO: Initialize a variable to keep track of the reversed number
reversed_num = 0
# TODO: Use a while loop to iterate and reverse the digits of the number
while num > 0:
    digit = num % 10 # Extracting last digit
    reversed_num = reversed_num * 10 + digit
    num //=10 # Remove last digit

# TODO: Print the reversed number
print("The reversed number is",reversed_num)