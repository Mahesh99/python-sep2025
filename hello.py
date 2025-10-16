print("Lakshith")
print("welcome to python classes")
print(1+2)
print(4-3)
print(3*4)
print(16/4)
print(6%4)
print(6//4)
print(2**3)
print(3**3)
x2=10
print(x2)
y=x2+2
print(y)
z=y+x2
print(z)
# not=10
not2=10
my_height=173
h=173
todays_max_temp=33



# Assignment Operators

# =
# +=
# -=
# *=
# /=
# %=
# //=
# **=

cs=10
cs=cs+4
cs+=4
cs+=1
cs+=5

b=15
b-=4
print(b)

b*=2
print(b)

b%=3
print(b)

f=1.4
print(type(f))
print(type(b))



# Data types
# int - ...-3, -2, -1, 0, 1, 2, 3...
# float - 1.2, 3.4, 5.6
# bool - True, False
# str - "hi","1","lakshith","123" - used to represent text

k=True
l=False
print(type(k))
is_raining=False

name="Pramanicus Academy"
student1="Lakshith"
student2='Charan'
print(type(name))
print(name)
print(student1)
print(student2)

temp="98.4"
#f=1.8*c+32
temp=float(temp) #98.4
c=(temp-32)/1.8
print(c)

# Type conversion
# Changing one data type to another
# int() - str 
# float() - str #int,float
# str() - int,float

wtemp="29"
# wtemp=int(wtemp)
wtemp=float(wtemp)
print(wtemp)

f=20.5
print(type(f))
s=str(f)
print(type(s))
print(f,s)

# Comparison Operators
# ==, !=, >, <, >=, <=
print(f==10.6)
print(10!=10)
print(5>10)
print(5<10)
print(6>=10)
print(7<=10)

print()
print()
# Logical Operators
# and, or, not
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print()
print(True or True)
print(True or False)
print(False or True)    
print(False or False)

print()
print(not True)
print(not False)

# Types of operators based on number of operands
# Unary - 1 operand
# Binary - 2 operands

# 5+4
# operand     operator     operand
#    5            +           3


# Type conversion
# float(), int(), str()

# int()
a=1.6
b=int(a)
c=int("12") # main
d="12"
# e="1.2"
# f=int(e)  # error
print(type(a),type(b),type(d))
print(b,c)

# print("74*5=",74*5)


# float()
a=1
b=float(a)
print(b)
c=float("12.5") # main
d=float("12") # main
print(c,d)

# str()
a=1.6
b=11
c= str(a) # "1.6"
d= str(b) # "11"
print(type(c),type(d))
print(a,b)
print(c,d)

print("sum of 2 and 3 is "+str(2+3))


# String operations
# +(concatenation), *(repetition)

s1="Hello"
s2="World"
s3=s1+s2
print(s3)
s3=s1+" "+s2
print(s3)

# "1" + "hello"
# 2+3.4
# 5+"hello" - error

g="hello"
f=g*5
print(f)

# Comments - is a line in a program that is ignored by the python interpreter
# Single line comment - #
# Multi line comment - '''...''' or """..."""


"""
This is a
multi line
comment
"""

'''This is a
multi line
comment
'''