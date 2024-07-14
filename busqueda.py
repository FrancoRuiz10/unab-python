#busqueda
lista=["a","b",1.5,4,"C"]
print(lista.index("a"))
# print(lista.index("z"))
print(2 in lista)
lista1 = ["a", "b", "c", "d", "x", "m"]

def buscar(lista_donde_buscar, valor_a_buscar):
    contador = 0
    for elemento in lista_donde_buscar:
        contador += 1
        if elemento == valor_a_buscar:
            print(contador)
            return True
        print(contador)
    return False  
    
print(buscar(lista1, "h"))

lista_ordenada=[1,2,3,4,5,6,7,8,9,10]
def buscar_en_dos_partes(lista_a_buscar,valor_a_buscar):
    indice_medio=len(lista_a_buscar)//2
    if valor_a_buscar>=lista_a_buscar[indice_medio]:
        buscar(lista_a_buscar[indice_medio:],valor_a_buscar)
    else:
        buscar(lista_a_buscar[:indice_medio],valor_a_buscar)

print(buscar(lista_ordenada,2))