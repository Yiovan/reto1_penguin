def inicializar(filas: int, columnas: int, modo_movimiento: int = 4):
    inicio_gato = (0, 0)
    inicio_raton = (filas - 1, columnas - 1)
    
    # ¡CORRECCIÓN DE SINTAXIS! Añadimos comas entre las tuplas
    movimientos_4 = [
        (-1, 0),  # arriba
        (1, 0),   # abajo
        (0, -1),  # izquierda
        (0, 1)    # derecha 
    ]
    
    # Las diagonales
    movimientos_8 = movimientos_4 + [
        (-1, -1), # arriba izquierda
        (-1, 1),  # arriba derecha
        (1, -1),  # abajo izquierda 
        (1, 1)    # abajo derecha
    ]
    
    if modo_movimiento == 8:
        movimientos = movimientos_8
    else:
        # COMPLETAR: Si no es 8, usa el modo por defecto (4)
        movimientos = movimientos_4 
        
    return inicio_gato, inicio_raton, movimientos



def mapa():
    FILAS = 5
    COLUMNAS = 5

    # 1. Obtener la inicialización del juego (usamos 8 direcciones)
    inicio_gato, inicio_raton, movimientos = inicializar(FILAS, COLUMNAS, modo_movimiento=8)
    
    # 2. Inicializar el tablero con espacios o un marcador de casilla vacía
    tablero_matriz = [['.' for _ in range(COLUMNAS)] for _ in range(FILAS)] 
        
    # 3. Colocar el Gato y el Ratón en sus posiciones iniciales
    tablero_matriz[inicio_gato[0]][inicio_gato[1]] = 'g' # Gato en (0, 0)
    tablero_matriz[inicio_raton[0]][inicio_raton[1]] = 'r' # Ratón en (4, 4)

    print("## 🗺️ Tablero Inicial")
    print("----------------------")
    for fila in tablero_matriz:
        print("| " + " | ".join(fila) + " |")
        
    print("\n##  Reglas de Movimiento")
    print(f"* Posición Gato (g): {inicio_gato}")
    print(f"* Posición Ratón (r): {inicio_raton}")
    print(f"* Movimientos del Ratón ({len(movimientos)} direcciones):")
    print(movimientos)
    movimientos= input("ingrese un movimiento /n")
    print(movimientos)
mapa()


def mover_pieza(posicion: tuple, tecla: str, filas: int, columnas: int):
    