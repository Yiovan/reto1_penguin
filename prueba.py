import random

def crear_laberinto(ancho, alto):
    # Crear una cuadrícula llena de paredes
    laberinto = [['#' for _ in range(ancho * 2 + 1)] for _ in range(alto * 2 + 1)]
    
    # Direcciones: arriba, derecha, abajo, izquierda
    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Pila para el backtracking
    pila = []
    visitados = set()
    
    # Empezar en (0, 0)
    celda_actual = (0, 0)
    visitados.add(celda_actual)
    pila.append(celda_actual)
    
    # Convertir coordenadas de celda a coordenadas del laberinto
    def celda_a_laberinto(fila, col):
        return fila * 2 + 1, col * 2 + 1
    
    # Marcar la celda inicial como camino
    lab_fila, lab_col = celda_a_laberinto(0, 0)
    laberinto[lab_fila][lab_col] = ' '
    
    while pila:
        fila, col = celda_actual
        
        # Encontrar vecinos no visitados
        vecinos_no_visitados = []
        for df, dc in direcciones:
            nueva_fila, nueva_col = fila + df, col + dc
            if (0 <= nueva_fila < alto and 
                0 <= nueva_col < ancho and 
                (nueva_fila, nueva_col) not in visitados):
                vecinos_no_visitados.append((nueva_fila, nueva_col))
        
        if vecinos_no_visitados:
            # Elegir un vecino aleatorio
            siguiente = random.choice(vecinos_no_visitados)
            siguiente_fila, siguiente_col = siguiente
            
            # Marcar como visitado
            visitados.add(siguiente)
            pila.append(siguiente)
            
            # Abrir el camino en el laberinto
            lab_fila_actual, lab_col_actual = celda_a_laberinto(fila, col)
            lab_fila_siguiente, lab_col_siguiente = celda_a_laberinto(siguiente_fila, siguiente_col)
            
            # Marcar la nueva celda como camino
            laberinto[lab_fila_siguiente][lab_col_siguiente] = ' '
            
            # Abrir la pared entre las celdas
            pared_fila = (lab_fila_actual + lab_fila_siguiente) // 2
            pared_col = (lab_col_actual + lab_col_siguiente) // 2
            laberinto[pared_fila][pared_col] = ' '
            
            celda_actual = siguiente
        else:
            # Backtrack
            if pila:
                pila.pop()
                if pila:
                    celda_actual = pila[-1]
    
    # Marcar entrada y salida
    laberinto[1][0] = '▶'  # Entrada
    laberinto[-2][-1] = '◀'  # Salida
    
    return laberinto

def imprimir_laberinto(laberinto):
    """Imprime el laberinto con mejor visualización"""
    print("\n" + "="*len(laberinto[0])*2)
    print("LABERINTO")
    print("▶ = Entrada, ◀ = Salida")
    print("="*len(laberinto[0])*2 + "\n")
    
    for fila in laberinto:
        for celda in fila:
            if celda == '#':
                print('██', end='')
            elif celda == '▶':
                print('▶ ', end='')
            elif celda == '◀':
                print('◀ ', end='')
            else:
                print('  ', end='')
        print()

def resolver_laberinto(laberinto):
    """Encuentra y marca la solución del laberinto"""
    # Hacer una copia para no modificar el original
    laberinto_solucion = [fila[:] for fila in laberinto]
    
    # Encontrar entrada
    entrada = None
    for i in range(len(laberinto_solucion)):
        for j in range(len(laberinto_solucion[0])):
            if laberinto_solucion[i][j] == '▶':
                entrada = (i, j)
                break
        if entrada:
            break
    
    # BFS para encontrar el camino
    from collections import deque
    
    cola = deque([entrada])
    padres = {entrada: None}
    visitados = {entrada}
    
    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    salida = None
    
    while cola:
        fila, col = cola.popleft()
        
        if laberinto_solucion[fila][col] == '◀':
            salida = (fila, col)
            break
        
        for df, dc in direcciones:
            nueva_fila, nueva_col = fila + df, col + dc
            
            if (0 <= nueva_fila < len(laberinto_solucion) and
                0 <= nueva_col < len(laberinto_solucion[0]) and
                (nueva_fila, nueva_col) not in visitados and
                laberinto_solucion[nueva_fila][nueva_col] != '#'):
                
                visitados.add((nueva_fila, nueva_col))
                padres[(nueva_fila, nueva_col)] = (fila, col)
                cola.append((nueva_fila, nueva_col))
    
    # Reconstruir el camino
    if salida:
        camino = []
        actual = salida
        while actual and actual != entrada:
            camino.append(actual)
            actual = padres.get(actual)
        
        # Marcar el camino con puntos
        for fila, col in camino:
            if laberinto_solucion[fila][col] not in ['▶', '◀']:
                laberinto_solucion[fila][col] = '·'
    
    return laberinto_solucion

# ====== PROGRAMA PRINCIPAL ======

# Configuración del laberinto
ancho = 15  # Número de celdas de ancho
alto = 10   # Número de celdas de alto

# Crear laberinto
laberinto = crear_laberinto(ancho, alto)

# Mostrar laberinto
imprimir_laberinto(laberinto)

# Preguntar si quiere ver la solución
print("\n¿Quieres ver la solución? (s/n): ", end='')
respuesta = input().lower()

if respuesta == 's':
    laberinto_resuelto = resolver_laberinto(laberinto)
    print("\n" + "="*len(laberinto[0])*2)
    print("SOLUCIÓN (· = camino)")
    print("="*len(laberinto[0])*2 + "\n")
    
    for fila in laberinto_resuelto:
        for celda in fila:
            if celda == '#':
                print('██', end='')
            elif celda == '▶':
                print('▶ ', end='')
            elif celda == '◀':
                print('◀ ', end='')
            elif celda == '·':
                print('··', end='')
            else:
                print('  ', end='')
        print()

# Generar múltiples laberintos
print("\n¿Generar otro laberinto? (s/n): ", end='')
if input().lower() == 's':
    # Simplemente vuelve a ejecutar el programa
    print("\nVuelve a ejecutar el programa para un nuevo laberinto!")