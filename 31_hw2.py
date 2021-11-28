# Write program to Find the square root of the number using in-built function.

number = int(input("Enter a number to find the square root : "))

if number < 0 :
  print("Please enter a valid number.")
else :
  sq_root = number ** 0.5
  print("Square root of {} is {} ".format(number,sq_root))