#Adivinar un color en Python
import random
words = ["Rojo","Verde","Azul"]
while True:
    pal = input ("Ingrese un Color:")
    n =random.randint(0, 2)
    if pal == words[n]:
        print("Muy bien, adivinaste La palabra!")
        break
    else:
        print("Intentalo nuevamente")
