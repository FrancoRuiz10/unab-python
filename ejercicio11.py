km_recorridos=float(input("Ingrese los kilometros recorridos: "))
precio=float(input("Ingrese el precio de la gasolina: "))
plata=float(input("Ingrese la plata de gasolina gastada en el viaje: "))
horas=int(input("Ingrese las horas que se ha tardado: "))
minutos=int(input("Ingrese los minutos adiciconales que se ha tardado: "))

consumo_100_km_litros=plata/(km_recorridos/100)
consumo_pesos=plata
consumo_litros=consumo_100_km_litros/100
consumo_km_pesos=consumo_pesos/km_recorridos
tiempo_hora=horas+minutos/60
velocidad=km_recorridos/tiempo_hora
velocidad_media=velocidad/100 
print(f"consumo de gasolina por cada 100 km: ")
print(f"-litros: {consumo_100_km_litros}")
print(f"- pesos: {consumo_pesos}")
print(f"consumo de gasolina por cada km: ")
print(f"-litros: {consumo_litros}")
print(f"-pesos {consumo_km_pesos}")
print(f"velocidad media: {velocidad_media}")
print(f"velocidad media en km/h: {velocidad}")