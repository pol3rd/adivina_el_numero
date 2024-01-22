import random

def adivina_el_número(x):
    
    print("=========================")
    print("¡Bienvenido(a) al juego! ")
    print("=========================")
    print("Tu meta es adivinar el número generado por la máquina.")

    número_aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x (incluyentes)

    predicción = 0

    while predicción != número_aleatorio:
        # El usuario ingresa un número
        predicción = int(input(f"Adivina un número entre uno y {x}: ")) #f-string

        if predicción < número_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif predicción > número_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")

    print(f"¡Felicidades! Has adivinado el número {número_aleatorio} correctamente.")

adivina_el_número(1520)