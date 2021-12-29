# 5. Get 5 marks as input from the user and calculate its average.
  
english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))
 
total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100
 
print("\nTotal Marks = %.2f"  %total)
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)
