class comprador:
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento, puntaje=0):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.puntaje = puntaje

    def sumar_puntos(self, puntos):
        self.puntaje += puntos

    def restar_puntos(self, puntos):
        self.puntaje -= puntos

#ejercicio 1.2
class Articulos:
    def __init__(self, identificador, nombre, descripcion, marca, precio, puntos):
        if identificador < 0:
            raise ValueError("El identificador debe ser un entero positivo.")
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos.")
        
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.precio = precio
        self.puntos = puntos

    def modificar_identificador(self, nuevo_identificador):
        if nuevo_identificador < 0:
            raise ValueError("El identificador debe ser un entero positivo.")
        self.identificador = nuevo_identificador

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def modificar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def modificar_marca(self, nueva_marca):
        self.marca = nueva_marca

    def modificar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def modificar_puntos(self, nuevos_puntos):
        if nuevos_puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos.")
        self.puntos = nuevos_puntos

        