import random

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.

    """
    
    numero_1 = str(random.randint(1, 10))
    numero_2 = str(random.randint(1, 10))
    numero_3 = str(random.randint(1, 10))
    numero_4 = str(random.randint(1, 10))
    numero_5 = str(random.randint(1, 10))
    numero_final = numero_1+numero_2+numero_3+numero_4+numero_5
    lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]

    print(lista_numeros)
    numero_1 = " "
    lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
    print(lista_numeros)
    numero_2 = " "
    lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
    print(lista_numeros)
    numero_3 = " "
    lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
    print(lista_numeros)
    numero_4 = " "
    lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
    print(lista_numeros)
    numero_5 = " "
    lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
    print(lista_numeros)
    print("")
    print("")
    print("")
    print("")
    print("")
    lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
    print(lista_numeros)
    print("¿¿¿¿¿¿ Qué números habían en la lista ???????")
    print("")
    print("ESCRIBA TODOS LOS NUMEMROS SEGUIDOS Y PRESIONE ENTER PARA COMPROBAR")
    adivinanza = input()

    if adivinanza == numero_final:
        print("¡¡¡¡¡FELICITACIONESSS GANASTE EL JUEGO. ERES UN CRACKKKK!!!!!!!!!")

    else:
        print("perdiste el juego. JUEGA DE NUEVO")
        memoria()    
memoria()