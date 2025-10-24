# string - used to represent text
s1="hello"
s2='hi'
s5=""
s6="Welcome to python programming. It's fun to learn python. Python is easy to learn. Python is powerful."

# multi line string creation
s3='''this type of string
creation is used
for multi line strings'''
s4="""this type of string
creation is used
for multi line strings"""
s7="""
Todo List:
1. Learn python basics
2. Graphics
3. Skating
4. Swimming
"""


print(s1)
print(s2)
print(s5)
print(s6)
print(s3)
print(s4)
print(s7)

k="\"Knowledge is power.\""
k='"Knowledge is power."'
print(k)

j='it\'s'
print(j)

# indexing

s="Hello World"

# H  e l l o   W o r l d
# 0 1 2 3 4 5 6 7 8 9 10
#-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(s[0])  # H
print(s[4])  # o
print(s[10]) # d
# print(s[11]) # d
print(s[-1])  # d

# len()
# function to find length of string
print(len(s)) # 11
print(len(s6))
print(len("hello everyone"))

# string methods
# lower() upper() captialize() title() strip() replace() find() count() etc.

s="  Hello World  "
s6="Welcome to python programming. It's fun to learn python. Python is easy to learn. Python is powerful."
# s6[1] = "M"  # This will raise an error since strings are immutable 

print(s.lower())
print(s.upper())
print(s6.capitalize())
print(s6.title())
print(s.strip())
print(s6.strip())
print(s6.replace("python","Java"))
print(s6.lower().replace("python","Java"))
print(s6.find("Python"))  # index of first occurrence
print(s6.index("Python"))  # index of first occurrence
print(s6.find("java"))  # index of first occurrence
# print(s6.index("java"))  # index of first occurrence
print(s6.count("python"))  # number of occurrences
print(s6.lower().count("python"))  # number of occurrences

#format(),capitalize()

name = "ARJUN"
favourite_color = "Navy Blue"
sentence = "{}'s favourite color is {}"
# print(sentence)
print(sentence.format(name,favourite_color))

print(sentence.format(name.capitalize(),favourite_color))
# print("{}'s favourite color is {}".format("ARJUN".capitalize(),"Navy Blue"))
# print("{}'s favourite color is {}".format("Arjun","Navy Blue"))
# print("Arjun's favourite color is Navy Blue")

l="all words are in lowercase"
print(l.islower())
print(s6.islower())

# any method name that starts with is  returns boolean value
print(l.isupper())
print(name.isupper())
print(s6.isupper())

n="12345"
m="123.45"
print(n.isdigit())
print(m.isdigit())

print(s6.isalnum())
print(n.isalnum())
print("Hello123".isalnum())
print("Hello 123".isalnum())
print(name.isalpha())

# f-strings (formatted string literals) - Python 3.6+
name = "ARJUN"
favourite_color = "Navy Blue"
sentence = f"{name}'s favourite color is {favourite_color}"
print(sentence)

print(f"this is a f-string {3*2} {name.lower()}")
print("this is a f-string 3*2 {name.lower()}")

# dir() help()
print(dir(str))
print(help(str.replace))
print(help(str.lower))
# print(help(str))


# slicing
s="Hello World"
s1=s[0:5]  # Hello
s2=s[:5]  # Hello
print(s1,s2,s)
print(s[8:11])
print(s[8:])

# step value
s3=s[::2]  # HloWrd
s3=s[0:11:3]  # HlWl
print(s3)

s4=s[::-1]  # reverse string
print(s4)
