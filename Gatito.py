import random

def mostrargatito(tablagato):
    print("\n     GATITO")
    print("  | 1 | 2 | 3 |")
    print(" -------------")
    print(f"1 | {tablagato[0]} | {tablagato[1]} | {tablagato[2]} |")
    print(" -------------")
    print(f"2 | {tablagato[3]} | {tablagato[4]} | {tablagato[5]} |")
    print(" -------------")
    print(f"3 | {tablagato[6]} | {tablagato[7]} | {tablagato[8]} |")
    print(" -------------")

def movimientos(tablagato, jugador):
    while True:
        try:
            movimiento = int(input(f"\nMovimiento del 1 al 9 (Jugador {jugador}): ")) - 1
            if 0 <= movimiento < 9 and tablagato[movimiento] == " ":
                break
            else:
                print("\nMovimiento inválido")
        except ValueError:
            print("\nEntrada no válida")

    tablagato[movimiento] = jugador

def ganador(tablagato, jugador):
    moneyshots = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinaciones in moneyshots:
        if all(tablagato[i] == jugador for i in combinaciones):
            return True
    return False

def jugar_pvc():
    tablagato = [" " for _ in range(9)]
    turno = 0

    while True:
        mostrargatito(tablagato)
        if turno % 2 == 0:
            movimientos(tablagato, 'X')
        else:
            sepueden = [i for i, x in enumerate(tablagato) if x == " "]
            movimiento = random.choice(sepueden)
            print("\nEl botsito ataca viste")
            tablagato[movimiento] = 'O'

        if ganador(tablagato, 'X'):
            mostrargatito(tablagato)
            print("\n X ganó")
            break
        elif ganador(tablagato, 'O'):
            mostrargatito(tablagato)
            print("\nO ganó")
            break
        elif " " not in tablagato:
            mostrargatito(tablagato)
            print("\nEmpate")
            break

        turno += 1

def jugar_pvp():
    tablagato = [" " for _ in range(9)]
    turno = 0

    while True:
        mostrargatito(tablagato)
        jugador = 'X' if turno % 2 == 0 else 'O'
        movimientos(tablagato, jugador)

        if ganador(tablagato, 'X'):
            mostrargatito(tablagato)
            print("\nX ganó")
            break
        elif ganador(tablagato, 'O'):
            mostrargatito(tablagato)
            print("\nO ganó")
            break
        elif " " not in tablagato:
            mostrargatito(tablagato)
            print("\nEmpate")
            break

        turno += 1

def gato():
    print("\nBienvenido al gatito\n")

    while True:
        print("   _______________GATO________________ ")
        print(" /|                                   |")
        print("| |    ♥♦♣♠  Menú de Opciones  ♥♦♣♠   |")
        print("| |...................................|")
        print("| |                                   |")
        print("| |   1. Nueva partida (PvC)          |")
        print("| |___________________________________|")
        print("| |                                   |")
        print("| |   2. Nueva partida (PvP)          |")
        print("| |___________________________________|")
        print("| |                                   |")
        print("| |   3. Chao peskao (Salir)          |")
        print("| |___________________________________|")
        opcion = input("\nModo de juego: ")

        if opcion == "1":
            jugar_pvc()
        elif opcion == "2":
            jugar_pvp()
        elif opcion == "3":
            print("\n   __________SALIR__________ ")
            print(" /|                         |")
            print("| |     Chao peskao    :p   |")
            print("| |                         |")
            print("| |_________________________|")
            print("|/__________________________/")
            break
        else:
            print("\nSelecciona '1', '2' o '3'.")

gato()
