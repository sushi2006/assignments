# Write program to Find whether a given number is divisible by 3 and 5.

lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if((i%3==0) & (i%5==0)):
      print(i)