# Se usa 'y' para la fila (arriba/abajo) y 'x' para la columna (izquierda/derecha)
raton_y = 0 
raton_x = 0 
gato_y = 4 
gato_x = 9
ancho = 10  # Columnas (movimiento 'a' y 'd')
largo = 5   # Filas (movimiento 'w' y 's')
# El espacio ahora debe ser el ancho + 2 para los bordes
espacio = '#' * (ancho + 2) 

# Se ha simplificado la estructura de impresión para que coincida con el 2D
while True:
    print(espacio) # Borde superior

    # Bucle exterior: Itera sobre las filas (largo)
    for y in range(largo):
        fila = "|"
        # Bucle interior: Itera sobre las columnas (ancho)
        for x in range(ancho):
            
            # Comprueba si la posición actual (x, y) es donde está el ratón
            if x == raton_x and y == raton_y:
                fila += "r"
            else:
                fila += "." 

            #el movimiento del raton debe ser similar 

            if x == gato_x and y == gato_y:
                fila += "g"
            else:
                fila += "."
        fila += "|"
        print(fila)

    print(espacio) # Borde inferior

    # Condición de victoria: El ratón llega a la esquina inferior derecha
    if raton_x == ancho - 1 and raton_y == largo - 1:
        print('¡ganaste boludo!')
        break
        
    print(f'w = arriba, s = abajo, a = izquierda, d = derecha, q = salir')
    movimiento = input('movimiento: ')

    # --- Lógica de Movimiento ---
    if movimiento == 'd':
        # Mover derecha (aumentar x), limitado por el ancho
        raton_x = min(raton_x + 1, ancho - 1) 

    elif movimiento == 'a':
        # Mover izquierda (disminuir x), limitado por 0
        raton_x = max(raton_x - 1, 0)
        
    elif movimiento == 'w':
        # Mover arriba (disminuir y), limitado por 0
        raton_y = max(raton_y - 1, 0)

    elif movimiento == 's':
        # Mover abajo (aumentar y), limitado por el largo
        raton_y = min(raton_y + 1, largo - 1)
        
    elif movimiento == 'q':
        break

    else:
       gato_x = min(raton_x)