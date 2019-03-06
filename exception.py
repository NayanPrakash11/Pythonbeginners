""" som exception handling """

""" my own exception raise"""
#raise Exception("hell wrong one")
""" handle exception divide by 0"""
try:
    a=int(input("Enter the first number :"))
    b=int(input("Enter second numbe :"))
    print(a/b)
except ZeroDivisionError:
    print("Idiot, you have try to divide with zero")
else:
    print("well done")
