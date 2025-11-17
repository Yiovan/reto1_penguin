# Variables del Ratón
raton_y = 0 
raton_x = 0 

# Dimensiones del Tablero
ancho = 10  # Columnas
largo = 5   # Filas
espacio = '#' * (ancho + 2) 

# Variables del Queso
# Lista de coordenadas (x, y) donde se ubicará el queso 'Q'
posiciones_queso = [
    (ancho - 1, 0),          # Arriba a la derecha
    (0, largo - 1),          # Abajo a la izquierda
    (ancho // 2, largo // 2), # En el centro
    (ancho // 4, largo // 4)  # Una posición extra
]
quesos_recolectados = 0 

while True:
    print(espacio) # Borde superior

    # Bucle de Dibujo del Tablero
    for y in range(largo):
        fila = "|"
        for x in range(ancho):
            
            # 1. Dibujar el Ratón 'r'
            if x == raton_x and y == raton_y:
                fila += "r"
            
            # 2. Dibujar el Queso 'Q'
            elif (x, y) in posiciones_queso:
                fila += "Q"
            
            # 3. Dibujar el Espacio Vacío '.'
            else:
                fila += "." 
        
        fila += "|"
        print(fila)

    print(espacio) # Borde inferior
    print(f'Quesos restantes: {len(posiciones_queso)}')

    # --- Condición de Victoria ---
    if not posiciones_queso:
        print(f'¡GANASTE BOLUDO! Recolectaste los {quesos_recolectados} quesos.')
        break
        
    print(f'w = arriba, s = abajo, a = izquierda, d = derecha, q = salir')
    movimiento = input('movimiento: ')

    # --- Lógica de Movimiento ---
    if movimiento == 'd':
        raton_x = min(raton_x + 1, ancho - 1) 
    elif movimiento == 'a':
        raton_x = max(raton_x - 1, 0)
    elif movimiento == 'w':
        raton_y = max(raton_y - 1, 0)
    elif movimiento == 's':
        raton_y = min(raton_y + 1, largo - 1)
    elif movimiento == 'q':
        break

    # --- Lógica de Recolección de Queso ---
    # Se comprueba la nueva posición del ratón
    if (raton_x, raton_y) in posiciones_queso:
        print("¡Ñam! ¡Comiste un queso!")
        posiciones_queso.remove((raton_x, raton_y))
        quesos_recolectados += 1  