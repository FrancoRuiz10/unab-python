import random

cantidad_numeros=50_000
pares=0
impares=0

for i in range(0,cantidad_numeros):
    valor=random.randint(0,100)
    if valor % 2 == 0:
        pares+=1
    else:
        impares+=1

print(F"en una muestra {cantidad_numeros} encontramos pares {pares}, impares {impares}")