import os
import time
import msvcrt   # permite leer teclas sin Enter en Windows


contador =8



lab = [
    "#####################", #1
    "#     #        #    #", #2
    "# ##  # ###### # ## #", #3
    "S #   #      # #    #", #4
    "# # ######## # ######", #5
    "# #   Q    # #      #", #6
    "# ####### ## ###### #", #7
    "#       #        #  #", #8
    "# ##### ######## # ##", #9
    "#  Q  #          #  #", #10
    "#####################" #11
    
]

#cuadro del raton
fila_raton = 2
columna_raton = 4
#cuadro del gato
fila_gato = 2
columna_gato= 7

movimientos = [(-1,0), (1,0), (0,-1), (0,1)]

def heuristica (gato, raton):
    dx = abs(gato[0]- raton[0])
    dy = abs(gato[1]- raton[1])
    return -(dx +dy)

def es_valido(f, c):
    if f < 0 or f >= len(lab): return False
    if c < 0 or c >= len(lab[f]): return False
    return lab[f][c] != "#"




def minimax(gato, raton, profundidad, esMax):
    if profundidad == 0:
        return heuristica(gato, raton)

    if esMax:   # turno del gato (MAX)
        mejor = -9999
        for dx, dy in movimientos:
            ng = (gato[0] + dx, gato[1] + dy) #ng = nuevo gato == nueva posicion del garo
            if not es_valido(*ng): 
                continue
            valor = minimax(ng, raton, profundidad - 1, False)
            mejor = max(mejor, valor)
        return mejor

    else:       # turno del ratón (MIN)
        mejor = 9999
        for dx, dy in movimientos:
            nr = (raton[0] + dx, raton[1] + dy)
            if not es_valido(*nr):
                continue
            valor = minimax(gato, nr, profundidad - 1, True)
            mejor = min(mejor, valor)
        return mejor


def mover_gato():
    global fila_gato, columna_gato
    mejor_valor = -9999
    mejor_mov = (fila_gato, columna_gato)

    for dx, dy in movimientos:
        ng = (fila_gato + dx, columna_gato + dy)
        if not es_valido(*ng): 
            continue
        valor = minimax(ng, (fila_raton, columna_raton), 3, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = ng

    fila_gato, columna_gato = mejor_mov


def dibujar():
    os.system("cls")
    for f in range(len(lab)):
        linea = list(lab[f])
        if f == fila_raton:
            linea[columna_raton] = "R"
        if f == fila_gato:
            linea[columna_gato] = "G"
        print("".join(linea))

while True:
    dibujar()
    
    
    if lab[fila_raton][columna_raton] == "Q":
        print("El ratón llegó al queso")
        break   
    elif fila_gato == fila_raton and columna_gato == columna_raton:
        print ('fallaste, el gato le comio a tu ratoncito')
        break
    elif lab[fila_raton][columna_raton]== "S":
        print('encontraste la salida')
        break
    # elif contador == 0:
    #         print('alcanzaste tu limite de veces')
    #         break
    if msvcrt.kbhit():             # si se presionó una tecla
        tecla = msvcrt.getch().decode("utf-8").lower()
        #lo que quiero lograr aca es que logre moverse arriba con w
        if tecla == "w" and lab[fila_raton - 1] [columna_raton] != "#":
            fila_raton -=1
        #ahora lo que debo hacer es mover abajo, para ello resto en la fila -1
        elif tecla == "s" and lab[fila_raton + 1] [columna_raton] != "#":
            fila_raton +=1
        elif tecla == "a" and lab[fila_raton] [columna_raton -1] != "#":
            columna_raton-=1
        elif tecla == "d" and lab[fila_raton][columna_raton +1] != "#":
            columna_raton +=1
        else: 
            print('movimiento invalido') 
        mover_gato()
        contador -=1
        if contador == 0:
             print('alcanzaste tu limite de veces')
             break
    time.sleep(0.01)
