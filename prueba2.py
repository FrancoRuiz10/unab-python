import random

suma=0

for j in range (0,100):
    valor=random.random()*10
    print(F"pasada n#{j} numero aleatorio generado {valor}")
    suma+=valor

print(F"la suma de aleatorio es {suma}")