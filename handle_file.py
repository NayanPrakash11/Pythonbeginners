""" handle I/O error """

try:
    txt=open("/Users/chris/pygit/text.txt", "w")
    try:
        txt.write("This is a test")
    finally:
        txt.close()

except NameError:
     print("Errrror, gick inte att open filen, kolla namnsättning")
except FileNotFoundError:
     print("Errrror, gick inte att hitta filen, kolla namnsättning")
except IOError:
    print("Errrror, gick inte att skriva till filen")

