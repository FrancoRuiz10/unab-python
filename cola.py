# cola= []
# cola.append("leandro")
# cola.append("zoe")
# cola.append("vanesa")
# print(cola.pop(0))
# print(cola)
# print(cola.pop(0))
# print(cola)
# print(cola.pop(0))

class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)

    def dequeue(self):
        if len(self.elementos) == 0:
            return None
        else:
            return self.elementos.pop(0)

    def is_empty(self):
        return len(self.elementos) == 0

    def first(self):
        if self.is_empty():
            return None
        else:
            return self.elementos[0]

cola_macdonalds = Cola()
cola_macdonalds.enqueue("gustavo")
cola_macdonalds.enqueue("nadia")
cola_macdonalds.enqueue("ezequiel")
print(cola_macdonalds.dequeue())  
print(cola_macdonalds.dequeue()) 
print(cola_macdonalds.dequeue()) 
