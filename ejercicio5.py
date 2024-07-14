class ListaEnlazadaCircular:
    """Clase Lista Enlazada Circular."""

    #-------- Clase Anidada - NODO ------------#
    class _Node:
        """Clase Nodo."""
        __slots__ = '_element', '_next' # optimiza el uso de memoria

        def __init__(self, element, next): 
            self._element = element # inicializar el contenido del Nodo
            self._next = next       # referencia al siguiente Nodo

    def __init__(self):
        """Crea una Lista Vacia.""" 
        self._head = None  # referencia a la "cabeza" de la lista
        self._size = 0     # cantidad de elementos
    
    def __len__(self):
        """Retorna el número de elementos de la Lista."""
        return self._size

    def is_empty(self):
        """Retorna VERDADERO si la Lista está Vacia."""
        return self._size == 0

    def append(self, x):
        """Agrega un elemento al final de la lista."""
        new_node = self._Node(x, None)
        if self.is_empty():
            new_node._next = new_node  # Apunta a sí mismo
            self._head = new_node
        else:
            tail = self._head
            while tail._next != self._head:
                tail = tail._next
            tail._next = new_node
            new_node._next = self._head
        self._size += 1

    def insert(self, i, x):
        """Agrega el elemento 'x' en la posición 'i'."""
        if i < 0 or i > self._size:
            raise IndexError('Índice fuera de rango.')
        new_node = self._Node(x, None)
        if i == 0:
            if self.is_empty():
                new_node._next = new_node
                self._head = new_node
            else:
                tail = self._head
                while tail._next != self._head:
                    tail = tail._next
                new_node._next = self._head
                self._head = new_node
                tail._next = self._head
        else:
            prev = self._head
            for _ in range(i - 1):
                prev = prev._next
            new_node._next = prev._next
            prev._next = new_node
        self._size += 1

    def remove(self, x):
        """Elimina la primera aparición de 'x' en la lista."""
        if self.is_empty():
            raise ValueError(f"{x} no está en la lista.")
        current = self._head
        prev = None
        for _ in range(self._size):
            if current._element == x:
                if prev is None:  # Eliminar la cabeza
                    if self._size == 1:
                        self._head = None
                    else:
                        tail = self._head
                        while tail._next != self._head:
                            tail = tail._next
                        self._head = self._head._next
                        tail._next = self._head
                else:
                    prev._next = current._next
                self._size -= 1
                return
            prev = current
            current = current._next
        raise ValueError(f"{x} no está en la lista.")

    def pop(self, i=None):
        """Borra el elemento que está en la posición 'i' y devuelve su valor."""
        if self.is_empty():
            raise IndexError('Lista vacía.')
        if i is None:
            i = self._size - 1
        if i < 0 or i >= self._size:
            raise IndexError('Índice fuera de rango.')
        current = self._head
        prev = None
        for _ in range(i):
            prev = current
            current = current._next
        if prev is None:  # Eliminar la cabeza
            if self._size == 1:
                self._head = None
            else:
                tail = self._head
                while tail._next != self._head:
                    tail = tail._next
                self._head = self._head._next
                tail._next = self._head
        else:
            prev._next = current._next
        self._size -= 1
        return current._element

    def index(self, x):
        """Devuelve la posición de la primera aparición de 'x' en la lista."""
        current = self._head
        for i in range(self._size):
            if current._element == x:
                return i
            current = current._next
        raise ValueError(f"{x} no está en la lista.")
