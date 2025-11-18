def mapa(personaje): 
    mapa = [[0 for _ in range(6)]for _ in range(3)]
    if personaje == 'r':
        pos_inicial= (2,2)
        mapa[2][2]= 'r'
    elif personaje == 'g':
        pos_inicial = (0,0)
        mapa[0][0] = 'g'


    movimientos ={
        'izquierda' :(-1,0),
        'derecha' :  (1,0),
        'arriba' :   (0,-1),
        'abajo' :    (0,1),
    }
    nuevos_movimientos = []
    for dx, dy in movimientos.values():
        x, y = pos_inicial
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 6:
            nuevos_movimientos.append((nx, ny))
    for fila in mapa:
        print(fila)

    return nuevos_movimientos


personaje = input(' ingrese G si quiere jugar como gato o R si quiere jugar como Raton')
movs = mapa (personaje)
print("movimientos posibles", movs)
    # for fila in range(3):
    #     lista = []
    #     for columna in range(6):
    #         lista.append(columna + fila)
    #     mapa.append(lista)




