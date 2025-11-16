def crear_mapa():
    return [[0 for _ in range(6)] for _ in range(3)]


def imprimir_mapa(mapa, pos):
    x, y = pos
    for i in range(3):
        fila = []
        for j in range(6):
            if (i, j) == (x, y):
                fila.append('P')
            else:
                fila.append('.')
        print(fila)


def mover(pos_actual, direccion):
    movimientos = {
        'd': (-1, 0),   # izquierda
        'a': (1, 0),    # derecha
        'w': (0, -1),   # arriba
        's': (0, 1),    # abajo
    }

    if direccion not in movimientos:
        return pos_actual

    dx, dy = movimientos[direccion]
    x, y = pos_actual
    nx, ny = x + dx, y + dy

    if 0 <= nx < 3 and 0 <= ny < 6:
        return (nx, ny)
    return pos_actual and 'no se puede'
#si el personaje se sale del mapa, ya sea quiere superar las 


mapa = crear_mapa()
pos = (2, 2)

while True:
    imprimir_mapa(mapa, pos)
    mov = input("Mover (w/a/s/d): ")
    pos = mover(pos, mov)
