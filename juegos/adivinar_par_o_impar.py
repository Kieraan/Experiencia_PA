import random

def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.

    """

    numero_random = random.randint(1, 10)
    print("¿Es el número par o impar?")
    print("escoja su opción : (impar=1 ; par=2)")
    opcion = int(input()) 
    


    if numero_random%2 == 0: #par
        if opcion == 1:
            print("NO ADIVINASTEE")

        elif opcion == 2:
            print("Adivinaste correctamente")
        else:
            print("escoge una opción válida >:( todo de nuevo")
            adivinar_par_o_impar()


    else: #imparpar
        if opcion == 1:
            print("ADIVINASTEE")

        elif opcion == 2:
            print("No Adivinaste correctamente")
        else:
            print("escoge una opción válida >:( todo de nuevo")
            adivinar_par_o_impar()


adivinar_par_o_impar()

    