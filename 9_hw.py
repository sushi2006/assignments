s = "This is a TEST String"
print('String in all lower case-',s.lower())
s = "This is a Test String"
print('String in all upper case-', s.upper())

s = "this is a TEST String"
print('String Capitalized-',s.capitalize())

s = "this is a TEST String"
print('String Title cased-',s.title())

s = "this is a test string"
#change only if not already in lower case
if not s.islower():
    s = s.lower()
else:
    print('String already in lower case')
print(s)

s = "This is a test String"
#change only if not already in upper case
if not s.isupper():
    s = s.upper()
else:
    print('String already in upper case')
print(s)
