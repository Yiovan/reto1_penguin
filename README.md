# 🐭 Juego del Laberinto: Ratón vs Gato

Un juego de laberinto en la terminal donde controlas a un ratón que debe escapar de un gato inteligente que usa el algoritmo Minimax para perseguirte.

## 🎮 Descripción

Eres un ratón (R) atrapado en un laberinto con un gato (G) que te persigue inteligentemente. Tu objetivo es llegar al queso (Q) o encontrar la salida (S) antes de que el gato te atrape o se te acaben los movimientos.

## 🚀 Características

- **IA del Gato**: Utiliza el algoritmo Minimax con profundidad 3 para tomar decisiones óptimas
- **Control en Tiempo Real**: Movimiento fluido usando las teclas WASD
- **Límite de Movimientos**: Tienes 8 movimientos para completar tu objetivo
- **Múltiples Condiciones de Victoria**: Alcanza el queso (Q) o encuentra la salida (S)

## 📋 Requisitos

- Python 3.x
- Windows (utiliza la librería `msvcrt` para captura de teclas)
- Librerías estándar: `os`, `time`, `msvcrt`

## 🎯 Cómo Jugar

### Instalación

1. Guarda el código en un archivo llamado `laberinto.py`
2. Asegúrate de estar en Windows (requerido por `msvcrt`)

### Ejecución

```bash
python game.py
```

### Controles

- **W**: Mover arriba
- **S**: Mover abajo
- **A**: Mover izquierda
- **D**: Mover derecha

## 🏆 Condiciones de Victoria/Derrota

### Victorias
- ✅ Alcanzar el queso (Q)
- ✅ Encontrar la salida (S)

### Derrotas
- ❌ El gato te atrapa (ocupa tu misma posición)
- ❌ Se acaban tus 8 movimientos

## 🧠 Algoritmo Minimax

El gato utiliza el algoritmo Minimax para decidir sus movimientos:

- **Profundidad**: 3 niveles de búsqueda
- **Heurística**: Distancia Manhattan negativa (busca minimizar distancia al ratón)
- **Estrategia**: El gato maximiza su valor, el ratón lo minimiza

### Función Heurística

```python
heuristica = -(|fila_gato - fila_raton| + |columna_gato - columna_raton|)
```

Cuanto más negativo el valor, más cerca está el gato del ratón.

## 🗺️ El Laberinto

```
#####################
#     #        #    #
# ### # ###### # ## #
S #   #      # #    #
# # ######## # ######
# #        # #      #
# ####### ## ###### #
#       #        #  #
# ##### ######## # ##
#  Q  #          #  #
#####################
```

**Leyenda:**
- `#`: Pared
- `R`: Ratón (jugador)
- `G`: Gato (IA)
- `Q`: Queso (objetivo)
- `S`: Salida (objetivo alternativo)

## 🔧 Personalización

Puedes modificar fácilmente:

- **Número de movimientos**: Cambia `contador = 8` al inicio del código
- **Profundidad del Minimax**: Modifica el valor `3` en `minimax(ng, (fila_raton, columna_raton), 3, False)`
- **Diseño del laberinto**: Edita la lista `lab` con tu propio diseño
- **Posiciones iniciales**: Ajusta `fila_raton`, `columna_raton`, `fila_gato`, `columna_gato`

## 📝 Notas Técnicas

- El juego limpia la pantalla en cada frame usando `os.system("cls")`
- La captura de teclas es no bloqueante gracias a `msvcrt.kbhit()`
- El delay de `0.05` segundos crea un efecto de actualización suave

## ⚠️ Limitaciones

- Solo funciona en **Windows** debido al uso de `msvcrt`
- Para Linux/Mac, se necesitaría reemplazar `msvcrt` con alternativas como `curses` o `keyboard`

## 🎓 Conceptos de IA Aplicados

- **Minimax**: Algoritmo de decisión en juegos de suma cero
- **Heurística**: Función de evaluación para estados del juego
- **Búsqueda con profundidad limitada**: Balance entre tiempo de cómputo y calidad de decisión

## 💻 Explicación del Código

### Estructura Principal

El código se organiza en varias secciones clave:

#### 1. **Inicialización del Laberinto**
```python
lab = [
    "#####################",
    "#     #        #    #",
    ...
]
```
El laberinto se representa como una lista de strings, donde cada carácter representa un elemento del mapa.

#### 2. **Variables de Estado**
- `fila_raton, columna_raton`: Posición actual del jugador
- `fila_gato, columna_gato`: Posición actual del perseguidor
- `contador = 8`: Límite de movimientos disponibles

#### 3. **Funciones Auxiliares**

**`es_valido(f, c)`**: Verifica si una posición es válida (dentro del mapa y no es pared)

**`heuristica(gato, raton)`**: Calcula la distancia Manhattan negativa entre el gato y el ratón. Mientras más negativo, más cerca están.

**`dibujar()`**: Limpia la pantalla y renderiza el estado actual del juego, colocando R (ratón) y G (gato) en sus posiciones correspondientes.

#### 4. **El Algoritmo Minimax** ⚡

Esta fue **la parte más complicada** del desarrollo. El algoritmo Minimax simula los movimientos futuros tanto del gato como del ratón para encontrar la mejor jugada:

```python
def minimax(gato, raton, profundidad, esMax):
    if profundidad == 0:
        return heuristica(gato, raton)
    
    if esMax:   # Turno del gato (MAX)
        mejor = -9999
        for dx, dy in movimientos:
            ng = (gato[0] + dx, gato[1] + dy)
            if not es_valido(*ng): 
                continue
            valor = minimax(ng, raton, profundidad - 1, False)
            mejor = max(mejor, valor)
        return mejor
    
    else:       # Turno del ratón (MIN)
        mejor = 9999
        for dx, dy in movimientos:
            nr = (raton[0] + dx, raton[1] + dy)
            if not es_valido(*nr):
                continue
            valor = minimax(gato, nr, profundidad - 1, True)
            mejor = min(mejor, valor)
        return mejor
```

**¿Por qué fue complicado?**
- Requiere pensar recursivamente: el gato simula sus movimientos Y los posibles movimientos del ratón
- El concepto de "MAX" y "MIN" alternándose en cada nivel es contraintuitivo al principio
- Balancear la profundidad de búsqueda: mucha profundidad = cálculos lentos, poca profundidad = decisiones menos inteligentes
- Manejar correctamente las validaciones de movimiento en cada nivel recursivo

#### 5. **Movimiento del Gato**

```python
def mover_gato():
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
```

Esta función evalúa cada movimiento posible del gato usando Minimax y elige el que tiene mejor valor.

#### 6. **Loop Principal del Juego**

El bucle `while True` maneja:
1. Dibujar el estado actual
2. Verificar condiciones de victoria/derrota
3. Capturar entrada del jugador (WASD) con `msvcrt`
4. Mover al ratón si la tecla es válida
5. Llamar a `mover_gato()` después de cada movimiento del jugador
6. Decrementar el contador de movimientos

### 🎯 La Parte Más Fácil: El Gato Siempre Ganaba

Curiosamente, **la parte más fácil fue hacer que el gato siempre ganara**. Una vez implementado el algoritmo Minimax correctamente:

- El gato automáticamente toma decisiones óptimas
- Con profundidad 3, puede "ver" 3 movimientos adelante
- La heurística de distancia Manhattan hace que siempre busque acercarse al ratón
- El ratón humano comete errores, el gato no

**El verdadero desafío** fue balancear el juego para que fuera posible ganar:
- Limitar la profundidad del Minimax a 3 (en lugar de más)
- Dar múltiples objetivos (queso Y salida)
- Diseñar un laberinto con rutas alternativas
- Establecer un límite de movimientos justo

### 🔍 Flujo de Ejecución

1. Jugador presiona una tecla (W/A/S/D)
2. El ratón se mueve si el movimiento es válido
3. Se llama a `mover_gato()`
4. `mover_gato()` evalúa 4 posibles movimientos usando Minimax
5. Minimax simula recursivamente 3 niveles de juego
6. El gato elige el movimiento con mejor heurística
7. Se verifica si hay victoria/derrota
8. El ciclo se repite

## 🤝 Mejoras Posibles

- [ ] Agregar poda Alpha-Beta para optimizar Minimax
- [ ] Soporte multiplataforma
- [ ] Niveles de dificultad (ajustando profundidad)
- [ ] Múltiples gatos
- [ ] Power-ups o ítems especiales
- [ ] Sistema de puntuación

---

¡Disfruta el juego y trata de escapar del gato! 🐭💨
