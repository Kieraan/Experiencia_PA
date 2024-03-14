import random

def cachipun():
    print("Escoga una acción:")
    print("1- Tijera")
    print("2- Piedra")
    print("3- Papel")
    while True:
        J_I = input("-")
        if J_I.isdigit():
            J_I = int(J_I)
            if 0 < J_I and J_I < 4:
                break
            else:
               print("Número no valido, intente de nuevo") 
        else:
            print("Número no valido, intente de nuevo")
    J_Maquina = random.randint(1,3)
    if J_Maquina == 1:
        J_M = "Tijera"
    elif J_Maquina == 2:
        J_M = "Piedra"
    elif J_Maquina == 3:
        J_M = "Papel"
    if J_I == 1:
        J = "Tijera"
    elif J_I == 2:
        J = "Piedra"
    elif J_I == 3:
        J = "Papel"
    print("El computador saco: "+J_M)
    if J == J_M:
        print("Empate")
    elif (J == "Tijera" and J_M == "Piedra") or (J == "Piedra" and J_M == "Papel") or (J == "Papel" and J_M == "Tijera"):
        print("Perdiste")
    elif (J == "Piedra" and J_M == "Tijera") or (J == "Papel" and J_M == "Piedra") or (J == "PTijera" and J_M == "Papel"):
        print("Ganaste")
    pass