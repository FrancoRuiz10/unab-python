#pilas implementadas con listas
# pila=[]
# pila.append("plato del desayuno")
# pila.append("plato del almuerzo")
# pila.append("plato de la merienda")
# pila.append("plato de la cena")
# pila.pop(len(pila)-1)
# print(pila)

class Pila:
    # Creo una pila vacía
    def __init__(self):
        self.elementos = [] 
    
    # Método para agregar un elemento al final 
    def push(self, elemento):
        self.elementos.append(elemento)
    
    # Método para remover y devolver el último elemento
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.elementos.pop()
        
    # Método para verificar si la pila está vacía
    def is_empty(self):
        return len(self.elementos) == 0

    # Método para devolver el último elemento sin removerlo
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.elementos[-1]
    
    def count(self):
        return len(self.elementos)

pila1=Pila()
pila1.push("primer elemento")
pila1.push("otro elemento")
pila1.push("ultimo elemento")
print(pila1.pop())
print(pila1.pop())
print(pila1.pop())