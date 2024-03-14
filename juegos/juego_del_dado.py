from random import randint

def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    puntos_jugador = 0
    puntos_cpu = 0
    while (puntos_jugador and puntos_jugador) < 30:
        input('Presione enter')
        # El jugador recibe puntos
        puntos_jugador += randint(1, 6)
        puntos_cpu += randint (1, 6)
        print(f'Puntos jugador: {puntos_jugador} \n Puntos CPU: {puntos_cpu}')
        
    if puntos_jugador >= 30:
        print('Jugador Gana')
    
    else:
        print('CPU gana')
        
    return