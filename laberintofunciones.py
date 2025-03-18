FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

# Función para crear el laberinto
def crear_laberinto():
    return [[False] * COLUMNAS for _ in range(FILAS)]

# Función para mostrar el laberinto
def mostrar_laberinto(laberinto, fila_jugador, columna_jugador):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end="")  # Jugador
            elif laberinto[i][j]:
                print("O ", end="")  # Meta
            else:
                print(". ", end="")  # Espacio vacío
        print()

# Función para mover al jugador
def mover_jugador(movimiento, fila_jugador, columna_jugador):
    if movimiento == 'w' and fila_jugador > 0:
        fila_jugador -= 1
    elif movimiento == 's' and fila_jugador < FILAS - 1:
        fila_jugador += 1
    elif movimiento == 'a' and columna_jugador > 0:
        columna_jugador -= 1
    elif movimiento == 'd' and columna_jugador < COLUMNAS - 1:
        columna_jugador += 1
    return fila_jugador, columna_jugador

# Función principal
def main():
    laberinto = crear_laberinto()
    fila_jugador, columna_jugador = 0, 0
    laberinto[META_FILA][META_COLUMNA] = True  # Meta

    while True:
        mostrar_laberinto(laberinto, fila_jugador, columna_jugador)

        if fila_jugador == META_FILA and columna_jugador == META_COLUMNA:
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break

        movimiento = input("\nIngrese movimiento (w: arriba, s: abajo, a: izq, d: der): ")
        fila_jugador, columna_jugador = mover_jugador(movimiento, fila_jugador, columna_jugador)

if __name__ == "_main_":
    main()