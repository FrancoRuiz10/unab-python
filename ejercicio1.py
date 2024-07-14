class stack:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size=0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self,elem):
        new_node= self._Node(elem, self._head)
        self._head = new_node
        self._size += 1
    def pop(self):
        if self.is_empty():
            raise Empty("La pila esta vacia")
        result=self._head._element
        self._head = self._head._next
        self._size -= 1
        return result
    def top(self):
        if self.is_empty():
            raise Empty("La pila esta vacia")
        return self._head._element
    
class Empty(Exception):
    pass