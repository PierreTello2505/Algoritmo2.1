#Hacer que el sistenma genere un numero aleatorio entre 1 y 10, luego hacer que el usuario adivine el numero. La aplicacion debe terminar cuando el usuario adivine.

import random

s=random.randint(1,10)

while True:
    n = int(input("Adivina jejejejejeje"))

    if n==s:
        print("Me frejaste")
        break
    else:
        print("Te falta Mascota")