""" exampale how you can use the format string
more to read here https://docs.python.org/3/library/string.html"""
numbers=1,3,45,567546,34251234557
print('Some numbers : {4},{3},{2},{1}'.format(*numbers))

#example on format with input
input("What is your name? ")
name=input
print('Hello {}. '.format(name))

""" combination of two lists in a dot format (.format) code"""

names=['Kalle', 'Bosse', 'Nisse']
ages=[56,17,93]
print('{0[1]} is {1[1]} years'.format(names, ages))


