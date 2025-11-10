raton = 0 #se inicia el punto de vista desde el punto 0 
gato = 0
ancho = 10
espacio = '#' *10
while True:
    tablero = ""
    for i in range(ancho):
        if i == raton:
            tablero += "r"
            
        else:
            tablero += "."       
    print('|' + espacio + '|')
    print('|' + tablero + '|')
    print('|' + espacio + '|')


    if raton == ancho -1:
        print('ganaste boludo')
        break
    print(f'a = izquierda, d = derecha, q = salir')
    movimiento = input('movimiento: ')

    if movimiento == 'd':
        raton = raton +1 
        if raton >=ancho:
            raton = ancho -1 

    elif movimiento== 'a':
        posicion = posicion -1
        if posicion <0 :
            posicion= 0
    elif movimiento == 'q':
        break
    elif movimiento != 'd' | movimiento != 'a':
        if i == gato :
            tablero+='g'
            if movimiento != 'a' | 'd':
                gato = gato +1 
            if gato >=ancho:
                gato = ancho -1 

















