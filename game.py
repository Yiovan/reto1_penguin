def mapa():
    FILAS= 5
    COLUMNAS = 5


    tablero_matriz = []

    # for i in range(FILAS):
    #     fila = [' ' for j in range (COLUMNAS)]
    #     tablero_matriz.append(fila)
        
    tablero_matriz = [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]   
        
    tablero_matriz[0][0] = 'r'
    tablero_matriz[1][2] = 'q'

    print ("tablero")
    for fila in tablero_matriz:
        print(fila)
        
mapa()


def inicializar(filas: int, columnas: int, modo_movimiento: int = 4):
    inicio_gato = (0,0)
    inicio_raton = (filas - 1, columnas -1 )
    movimentos_4 =[
        (-1,0), #arriba
        (1,0), #abajo
        (0,-1) #izquierda
        (0,1) # derecha 
    ]
    ''' 
    seguir con movimientos diagonales mas tarde 
    '''
    movimentos_8 = [
        (-1,-1) #arriba izquierda
        (-1, 1) #arriba derecha
        (1,-1) #abajo izquierda 
        (1,1) #abajo derecha
    ]
    