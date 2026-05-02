import random

caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

contraseña_longitu = int(input("Introdusca la longuitud de su contraeña"))

contraseña = ""

for i in range(contraseña_longitu):

    contraseña += random.choice(caracter)

print(contraseña)