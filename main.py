# Python Variables - Assign Multiple Values

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python - Output Variables

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
# print(x + y) this will give an error 'int' and 'str' cannot be concatenated

# best way to output miltiple variables in print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)
# In the print() function, when you try to combine a string and a number with a + sign, Python will give you an error:


