class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.next = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.len = 0

    # Inserta un nodo al inicio de la lista
    def insertarAlInicio(self, nodo):
        if self.primero is None:
            self.primero = nodo
        else:
            nuevo_nodo = self.primero
            self.primero = nodo
            self.primero.next = nuevo_nodo
        self.len += 1

    # Insertar al final
    def insertarAlFinal(self, nodo):
        if self.primero is None:
            self.primero = nodo
        else:
            nodo_temporal = self.primero
            while nodo_temporal.next is not None:
                nodo_temporal = nodo_temporal.next
            nodo_temporal.next = nodo
        self.len += 1

    # Devuelve la posición del elemento, o Excepción si no lo encuentra
    def posicionElemento(self, valor):
        if self.primero is None:
            raise Exception("Lista vacía")
        else:
            posicion = 0
            if self.primero.dato == valor:
                return posicion
            else:
                nodo_temporal = self.primero
                while nodo_temporal.next is not None:
                    nodo_temporal = nodo_temporal.next
                    posicion += 1
                    if nodo_temporal.dato == valor:
                        return posicion
            raise Exception("Valor no encontrado!!")

    # Devuelve y remueve el primer elemento
    def remuevePrimerElemento(self):
        if self.primero is None:
            raise Exception("La Lista está Vacía")
        else:
            nodo_temporal = self.primero
            self.primero = self.primero.next
            self.len -= 1
            return nodo_temporal

    # Devuelve y remueve el último elemento
    def remueveUltimoElemento(self):
        if self.primero is None:
            raise Exception("La Lista está Vacía")
        if self.primero.next is None:
            nodo_a_devolver = self.primero
            self.primero = None
            self.len -= 1
            return nodo_a_devolver

        nodo_temporal = self.primero
        while nodo_temporal.next.next is not None:
            nodo_temporal = nodo_temporal.next
        nodo_a_devolver = nodo_temporal.next
        nodo_temporal.next = None
        self.len -= 1
        return nodo_a_devolver

    # Remueve un elemento por valor
    def remueveElemento(self, valor):
        if self.primero is None:
            raise Exception("La Lista está Vacía")
        if self.primero.dato == valor:
            return self.remuevePrimerElemento()
        
        nodo_temporal = self.primero
        while nodo_temporal.next is not None:
            if nodo_temporal.next.dato == valor:
                nodo_a_remover = nodo_temporal.next
                nodo_temporal.next = nodo_temporal.next.next
                self.len -= 1
                return nodo_a_remover
            nodo_temporal = nodo_temporal.next
        raise Exception("Valor no encontrado!!")

    # Remueve un elemento por índice
    def remueveIndice(self, indice):
        if indice < 0 or indice >= self.len:
            raise IndexError("Índice fuera de rango")
        if indice == 0:
            return self.remuevePrimerElemento()

        nodo_temporal = self.primero
        for i in range(indice - 1):
            nodo_temporal = nodo_temporal.next
        nodo_a_remover = nodo_temporal.next
        nodo_temporal.next = nodo_temporal.next.next
        self.len -= 1
        return nodo_a_remover

    # Devuelve el elemento en la posición especificada
    def elementoPorIndice(self, indice):
        if indice < 0 or indice >= self.len:
            raise IndexError("Índice fuera de rango")

        nodo_temporal = self.primero
        for i in range(indice):
            nodo_temporal = nodo_temporal.next
        return nodo_temporal.dato

    # Representación en forma de string de la ListaEnlazada
    def __str__(self):
        if self.primero is None:
            return "[]"
        else:
            str_lista = "[ "
            nodo = self.primero
            str_lista += str(self.primero.dato)
            while nodo.next is not None:
                nodo = nodo.next
                str_lista += " "
                str_lista += str(nodo.dato)
            str_lista += " ]"
            return str_lista



my_lista = ListaEnlazada()
print(my_lista.len)
print(my_lista)
# my_lista.posicionElemento(1)

nodo_x = Nodo(3)
my_lista.insertarAlInicio(nodo_x)

nodo_y = Nodo(9)
my_lista.insertarAlInicio(nodo_y)

print(my_lista.len)
print(my_lista)

my_lista.insertarAlFinal(Nodo(0))
print(my_lista)

print(my_lista)

nodo_final = my_lista.remueveUltimoElemento()
nodo_final.dato

my_lista2 = ListaEnlazada()
my_lista2.insertarAlFinal(Nodo(1))
nodo = my_lista2.remueveUltimoElemento()
nodo.dato

my_lista.posicionElemento(9)

nodo = my_lista.remuevePrimerElemento()
nodo.dato

print(my_lista)

my_lista.len
my_lista.remuevePrimerElemento()
print(my_lista)

my_lista.remuevePrimerElemento()
my_lista.len
my_lista.remuevePrimerElemento()