class ColaEnlazada:

#-------- Clase Anidada - NODO ------------#
  class _Node:
    __slots__ = '_element', '_next' # optimiza el uso de memoria

    def __init__(self, element, next): 
      self._element = element # inicializar el contenido del Nodo
      self._next = next       #referencia al siguiente Nodo

#----------- Métodos de la Cola ----------- #

  def __init__(self):
    self.elementos=[]
    self._head = None
    self._tail = None
    self._size = 0  # Numero de elementos en la Cola 

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0

  def first(self):
        if self.is_empty():
           raise Exception("La cola esta vacia")
        return self._head._element
        
    # COMPLETAR #

  def dequeue(self):
        if self.is_empty():
          raise Exception("La cola esta vacia")
        result=self._head._element # devuelve el primer elemento de la cola
        self.head=self._head._next
        self._size -= 1
        if self.is_empty():
          self._tail=None
        return result
  
  def enqueue(self, e):
    new_mode=self._Node(e) # crea un nuevo nodo sin siguiente nodo
    if self.is_empty():
       self._head=new_mode # si la cola está vacía, la cabeza es el nuevo nodo
    else:
       self._tail._next=new_mode # de lo contrario, el último nodo apunta al nuevo nodo
    self._tail=new_mode  # actualiza la cola para que el último nodo sea el nuevo nodo
    self._size += 1  # incrementa el tamaño de la cola
    
    # COMPLETAR #