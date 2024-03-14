from random import randint

def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    numero_aleatorio = randint(1,10)
    seleccion = int(input('Seleccione un número entre 1 y 10: '))
    if numero_aleatorio == seleccion:
        print(f'El número escogido es correcto: {seleccion}')
        
    else:
        print('El número escogido es incorrecto')
    
    return 
