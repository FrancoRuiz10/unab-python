class nodo:
    def __init__(self,valor=None, prox=None):
        self.valor = valor
        self.prox = prox
    def __str__(self):
        return  f"este es el nodo {self.valor}" 
    
nodo1=nodo(valor=0)
nodo2=nodo(valor=1)
nodo1.prox=nodo2
nodo3=nodo(valor=2)
nodo2.prox=nodo3
print(nodo1)
print(nodo1.prox)

nodo=nodo1
print(nodo.valor)
while(nodo.prox is not None):
    nodo= nodo.prox
    print(nodo.valor)

nodo=nodo1
a_encontrar=9
encontrado=False

if nodo.valor==a_encontrar:
    print(f"valor encontado en {nodo}")
else:
    while(nodo.prox is not None):
        nodo=nodo.prox
    if nodo.valor==a_encontrar:
        print(F"valor encontrado!!! en{nodo}")
        encontrado= True

