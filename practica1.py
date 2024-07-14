class Marciano:
    def __init__(self, nombre, ojos, piernas, color):
        self.nombre = nombre
        self.ojos = ojos
        self.piernas = piernas
        self.color = color

    def __str__(self):
        return F"el marciano {self.nombre} tiene {self.ojos} ojos, {self.piernas} piernas y es de color {self.color}"

    def __del__(self):
        print(F"Se murio el marciano {self.nombre}")
#Instaciar dos objetis dek tipo Marciano
marciano1=Marciano("Pedro" , 3, 4,"Azul")
marciano2=Marciano("Et", 1,7,"Verde")

#Mostrar los atributos de ambos
print(F"{marciano2}")
print(F"El marcianano 1 es de color {marciano1.color}")
print(F"El marciano 2 es de color {marciano2.color}")
del[marciano1]