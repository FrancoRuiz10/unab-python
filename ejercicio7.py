class ListaDoblementeEnlazada:

    #-------- Clase Anidada - NODO ------------#
    class _Node:
        __slots__ = '_element', '_prev', '_next'  # optimiza el uso de memoria

        def __init__(self, element, prev=None, next=None):
            self._element = element  # inicializar el contenido del Nodo
            self._next = next        # referencia al siguiente Nodo
            self._prev = prev        # referencia al Nodo anterior

    def __init__(self):
        self._head = None  # referencia a la "cabeza" de la lista
        self._tail = None  # referencia a la "cola" de la lista
        self._size = 0     # cantidad de elementos

    def __len__(self):
        """Retorna el número de elementos de la Lista."""
        return self._size

    def is_empty(self):
        """Retorna VERDADERO si la Lista está vacía."""
        return self._size == 0

    def append(self, x):
        """Agrega el elemento 'x' al final de la lista."""
        new_node = self._Node(x, self._tail, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def insert(self, i, x):
        """Agrega el elemento 'x' en la posición 'i'."""
        if i < 0 or i > self._size:
            raise IndexError("Índice fuera de rango")
        if i == self._size:
            self.append(x)
        else:
            current = self._head
            for _ in range(i):
                current = current._next
            new_node = self._Node(x, current._prev, current)
            if current._prev is None:  # inserting at the head
                self._head = new_node
            else:
                current._prev._next = new_node
            current._prev = new_node
            self._size += 1

    def remove(self, x):
        """Elimina la primera aparición de 'x' en la lista."""
        current = self._head
        while current is not None and current._element != x:
            current = current._next
        if current is None:
            raise ValueError(f"El elemento {x} no se encuentra en la lista")
        if current._prev is None:  # removing head
            self._head = current._next
        else:
            current._prev._next = current._next
        if current._next is None:  # removing tail
            self._tail = current._prev
        else:
            current._next._prev = current._prev
        self._size -= 1

    def pop(self, i=None):
        """Borra el elemento que está en la posición 'i' y devuelve su valor."""
        if self.is_empty():
            raise IndexError("La lista está vacía")
        if i is None:
            i = self._size - 1
        if i < 0 or i >= self._size:
            raise IndexError("Índice fuera de rango")
        current = self._head
        for _ in range(i):
            current = current._next
        value = current._element
        if current._prev is None:  # removing head
            self._head = current._next
        else:
            current._prev._next = current._next
        if current._next is None:  # removing tail
            self._tail = current._prev
        else:
            current._next._prev = current._prev
        self._size -= 1
        return value

    def index(self, x):
        """Devuelve la posición de la primera aparición de 'x' en la lista."""
        current = self._head
        position = 0
        while current is not None:
            if current._element == x:
                return position
            current = current._next
            position += 1
        raise ValueError(f"El elemento {x} no se encuentra en la lista")

# Ejemplos de uso
lista = ListaDoblementeEnlazada()
lista.append(1)
lista.append(2)
lista.append(3)
print(len(lista))  # Salida: 3
lista.insert(1, 4)
print(lista.pop(1))  # Salida: 4
print(lista.index(3))  # Salida: 2
try:
    lista.remove(5)
except ValueError as e:
    print(e)  # Salida: El elemento 5 no se encuentra en la lista
