# 4. Write a program to calculate the sum of all numbers from 1 to a given number.

num = int(input( "enter a integer: " ))
sum_num =0

if num != 0:
   for i in range(1, num+1): 
       sum_num += i
       print(sum_num)
else:
     exit()