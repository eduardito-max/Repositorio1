import random as r
import string as s

elements = s.ascii_letters + s.digits + s.punctuation
lenght =  int(input("introduce la longitud de tu contraseña: "))

pasword = ""
for i in range(lenght):
    pasword += r.choice(elements)
print(pasword)

