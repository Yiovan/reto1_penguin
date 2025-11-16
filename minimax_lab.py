class position:
    def __init__(self, r, g):
        self.r = r 
        self.c = c
    def __eq__(self, other):
        if not isinstance(other, position):
            return NotImplemented
        return self.r == other.r and self.c == other.c
    def __hash__(self):
        return hash ((self.r, self.c))
    def __str__ (self):
        return f'({self.r}, {self.c})'
    


print("--- 1. Prueba de Igualdad Lógica (==) ---")
# Creamos dos objetos que representan la misma casilla (3, 5), pero son instancias separadas
pos_gato = Position(3, 5)
pos_raton = Position(3, 5)

print(f"Posición Gato: {pos_gato}")
print(f"Posición Ratón: {pos_raton}")