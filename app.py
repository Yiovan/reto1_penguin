import random

# Definición de la matriz (un mapa simple 5x5)


def generar_mapa_aldeatorio(dimension=5, densidad_de_obstaculos= 0.2):
    if dimension < 3:
        raise ValueError("El tamaño del mapa debe ser al menos 3x3.")
    
    mapa = []
    for i in range(dimension):
            fila = []
            for j in range(dimension):
                # Usar random.random() para decidir si colocar un obstáculo
                if random.random() < densidad_de_obstaculos:
                    fila.append('#')
                else:
                    fila.append('.')
            mapa.append(fila)
    todas_posiciones = [(r,c) for r in range(dimension) for c in range(dimension)]
    posiciones_pe = random.sample(todas_posiciones, 2)
    posicion_inicial_p = list(posiciones_pe[0])
    punto_final_e = list(posiciones_pe[1])


    mapa[posicion_inicial_p[0]][posicion_inicial_p[1]]

    return mapa, posicion_inicial_p, punto_final_e






def mover(direccion):
    global posicion_actual

    if posicion_actual == punto_final:
        return True
    
    fila_anterior, col_anterior = posicion_actual[0], posicion_actual[1]
    nueva_fila, nueva_col = fila_anterior, col_anterior

    direccion = direccion.upper()
    if direccion == 'W':
        nueva_fila -= 1
    elif direccion == 'S':
        nueva_fila += 1
    elif direccion == 'A':
        nueva_col -= 1
    elif direccion == 'D':
        nueva_col += 1
    else:
        print("Dirección no válida. Usa W, A, S, o D.")
        return False


    if (0 <= nueva_fila <= MAX_FILA) and (0 <= nueva_col <= MAX_COLUMNA):
        
        if MAPA_JUEGO[nueva_fila][nueva_col] == '#':
            print("¡Movimiento bloqueado! Hay un obstáculo (#).")
            return False
            
        if [fila_anterior, col_anterior] == PUNTO_FINAL:
             MAPA_JUEGO[fila_anterior][col_anterior] = 'E' 
        else:
            MAPA_JUEGO[fila_anterior][col_anterior] = '.'
        
        posicion_actual[0] = nueva_fila
        posicion_actual[1] = nueva_col
        
        if posicion_actual == PUNTO_FINAL:
            MAPA_JUEGO[nueva_fila][nueva_col] = 'P' 
            mostrar_mapa()
            print("\n🎉🎉🎉 ¡FELICIDADES! ¡HAS LLEGADO AL PUNTO FINAL (E)! 🎉🎉🎉")
            return True
        
        MAPA_JUEGO[nueva_fila][nueva_col] = 'P'
        
        print(f"Movido a {direccion}.")
        return False
    else:
        print("¡Movimiento fuera de los límites de la matriz!")
        return False
# #MAPA = [
#     ['.', '.', '.', '.', '.'],
#     ['.', '#', '.', '#', '.'],
#     ['.', '.', 'P', '.', '.'],
#     ['.', '#', '.', '#', '.'],

#     ['.', '.', '.', '.', 'E'] # 'E' es el punto final
# ]

# # 1. Posición inicial del jugador (Fila, Columna)
# posicion_actual = [2, 2] 

# # Límites de la matriz
# MAX_FILA = len(MAPA) - 1
# MAX_COLUMNA = len(MAPA[0]) - 1

# # 2. Definir el punto final
# # Es la última fila y la última columna de la matriz.
# PUNTO_FINAL = [MAX_FILA, MAX_COLUMNA] 

def mostrar_mapa():
    """Imprime el mapa actual en la consola."""
    print("\n--- MAPA ---")
    for fila in MAPA:
        print(' '.join(fila))
    print("------------")
    print(f"Posición actual: Fila {posicion_actual[0]}, Columna {posicion_actual[1]}")

def mover(direccion):
    """
    Actualiza la posición del jugador basada en la dirección (W, A, S, D)
    y verifica si ha llegado al punto final.
    """
    global posicion_actual
    
    # Si ya ganamos, no permitimos más movimiento
    if posicion_actual == PUNTO_FINAL:
        print("¡Ya has completado el laberinto!")
        return
        
    fila_anterior, col_anterior = posicion_actual[0], posicion_actual[1]
    nueva_fila = fila_anterior
    nueva_col = col_anterior
    
    # 3. Calcular la nueva posición
    if direccion.upper() == 'W':
        nueva_fila -= 1
    elif direccion.upper() == 'S':
        nueva_fila += 1
    elif direccion.upper() == 'A':
        nueva_col -= 1
    elif direccion.upper() == 'D':
        nueva_col += 1
    else:
        print("Dirección no válida. Usa W, A, S, o D.")
        return

    # 4. Verificación de Límites y Obstáculos
    if (0 <= nueva_fila <= MAX_FILA) and (0 <= nueva_col <= MAX_COLUMNA):
        
        # Verificar obstáculo
        if MAPA[nueva_fila][nueva_col] == '#':
            print("¡Movimiento bloqueado! Hay un obstáculo (#).")
            return
            
        # 5. Actualización de Posición (Movimiento exitoso)
        
        # Dejar la posición anterior (reemplazar con '.' o 'E' si era el punto final)
        if [fila_anterior, col_anterior] == PUNTO_FINAL:
             MAPA[fila_anterior][col_anterior] = 'E' # Si te mueves del final, el final sigue siendo 'E'
        else:
            MAPA[fila_anterior][col_anterior] = '.'
        
        # Actualizar la posición global
        posicion_actual[0] = nueva_fila
        posicion_actual[1] = nueva_col
        
        # 6. Detección de Victoria
        if posicion_actual == PUNTO_FINAL:
            MAPA[nueva_fila][nueva_col] = 'P' # Coloca el jugador en la posición final
            mostrar_mapa()
            print("\n🎉🎉🎉 ¡FELICIDADES! ¡HAS LLEGADO AL PUNTO FINAL (E)! 🎉🎉🎉")
            return
        
        # Dibujar la 'P' en la nueva posición
        MAPA[nueva_fila][nueva_col] = 'P'
        
        print(f"Movido a {direccion.upper()}.")
    else:
        print("¡Movimiento fuera de los límites de la matriz!")

# --- DEMOSTRACIÓN DEL MOVIMIENTO HACIA EL FINAL ---
movimiento= input('ingrese un movimiento')
mostrar_mapa()
while True:
    if movimiento== [4,4]:
        mostrar_mapa()
        print('ganaste')
        break
    else:
        mostrar_mapa()
        movimiento= input('ingrese un movimiento')
        

    mover(movimiento) # [3, 2]

# mover('W') # Intento de movimiento después de la victoria



