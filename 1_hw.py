
# 1. Get 2 numbers, input as a string, convert them to integer and add the two values
# 2. Swapping two numbers
# 3. Check if the input string is available in another string. (Example: Find 'mars' inside 'Hello mars')
# 4. Check current year is a leap year or not
# 5. Print the current date.
# 6. Reversing a string using python in-built methods
# 7. Split a string by space (Input: "Hello mars", Output: "Hello", "mars")
# 8. Check current number is odd or even using if condition
# 9. Converting a string from upper case to lower case.
# 10. Find letters count in a string

def add (a, b):
    return a + b

P = int( input("Please enter value for P: "))
Q = int( input("Please enter value for Q: "))
P = P ^ Q
Q = P ^ Q
P = P ^ Q
print ("The Value of P after swapping: ", P)
print ("The Value of Q after swapping: ", Q)

word = 'Hello mars'
result = word.find ('mars')
print ("substring 'mars' found at index:", result)

Year = int(input("Enter the Year:"))
if((Year%400 == 0) or ((Year%4 == 0) and (Year%100 != 0))):
    print("%d is a Leap Year" %Year)
else:
    print("%d is not a Leap Year" %Year)