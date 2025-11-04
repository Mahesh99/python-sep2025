# basic data types
# int, float, str, bool

# Data Structures 
#  list, tuple, set, dict

# list
# creating a list
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)

stds=["lakshith","charan","mahesh","rishi","manu"]
print(stds)

l=[1,2.5,"hello",True,3.14]
print(l)

l2=[]

# similar to strings list also supports indexing and slicing
# accessing elements using indexing
print(fruits[0])  # apple
print(fruits[1]) # banana
print(fruits[-1]) # date

# modifying elements in a list
fruits[1]="mango"
print(fruits)

# List functions
# len(), max(), min(), sum(), join()
# len() function to find number of elements in a list
print("fruits",len(fruits)) # 4
print(len(stds)) # 5
print(len(l)) # 5

# max() function to find the largest element in a list
numbers = [10, 5, 8, 20, 3]
print(max(numbers))

# min() function to find the smallest element in a list
print(min(numbers))

print(max(fruits))  # based on alphabetical order
print(min(fruits))

# sum() function to find the sum of elements in a list
print(sum(numbers))
# print(sum(fruits))  # will raise an error

print(sum(numbers)/len(numbers))  # average

# join() function to join elements of a list into a string
new_str = "--".join(fruits)
print(new_str)
print(type(new_str))
print(type(fruits))
print(fruits[0].upper())

# slicing
stds=["lakshith","charan","mahesh","rishi","manu"]
s1=stds[1:4]  # ['charan', 'mahesh', 'rishi']
s2=stds[:] # ['lakshith', 'charan', 'mahesh', 'rishi', 'manu']
print(s1)
print(s2)

std2=stds[::2]
print(std2)


# list methods
# append(), insert(), remove(), pop(), sort(), reverse(), clear(), extend()
l=[5,2,8,1,4,5]
print(l)
l.remove(5)  # removes first occurrence of 5
# l.remove(5)  # removes first occurrence of 5
# l.remove(5)  # removes first occurrence of 5
# print(l)
# l.sort()
print(l)
l.sort(reverse=True)
print(l)

l=l[::-1]
# l.reverse()
print(l)

j=[10,20,30]
l.extend(j)
print(l)


l.clear()
print(l)

# tuple, set, dict
# tuple


point = (4,3,11) # (x,y,z) coordinates in a 3d space
location = (17.393549, 78.533836) #(latitude, longitude)
dimens = 10,20,15 # (l,b,h) dimensions of a cuboid. Tuple can also be intialized this way
print(type(dimens))

l,b,h = dimens # Tuple unpacking
print(l,b,h)
print(dir(point))

# set
s={1,2,3,4,5,5,4,3}
print(s)
# print(s[0]) # will raise an error


fav_actors = ["Prabhas","Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naani",
                   "Ram Charan","Rakul Preeth","Samantha","Rakul Preeth","Prabhas","Samantha",
                  "Nivedha Thomas","Naaga chaithanya","Salman khan","Salman khan","Vijay","Shradha kapoor","Vijay",
                  "Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naaga chaithanya","Salman khan"]
print(len(fav_actors))
unique_fav_actors = set(fav_actors)
print(unique_fav_actors,len(unique_fav_actors))

actors=list(unique_fav_actors)
print(actors)

# set(), list(), tuple() type conversion functions

print(dir(set))

# set methods
# add(), union(), intersection(), remove(), pop()
s={11,22,3,4,5}
s.add(10)
print(s)
s2={11,20,13,5}
s3=s.union(s2)
print(s3)

s4=s.intersection(s2)
print(s4)
print(s.pop())
print(s.pop())
print(s.pop())

# print(help(set.pop))

# dictionary

#creating a dictionary
std={"name":"Lakshith","course":"python","duration":60,"fee":6000}
std2={"name":"charan","course":"python","duration":60,"fee":6000}

#accessing
print(std["name"])
print(std["fee"])

#modifying
std["duration"]=45
std["fee"]=6500
std["batch"]="sep-2025"

print(std,std2)

std_list=[std,std2]
print(std_list)

print(std_list[0]["name"])
print(std_list[1]["name"])

# in
print("name" in std)
print("fee" in std)
print("age" in std)
print(6000 in std)

# key(), values()
print(std.keys())
print(std.values())
