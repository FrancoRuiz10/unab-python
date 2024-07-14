def asignar_expedientes(expedientes):
    buzones = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J'}
    asignaciones = {}
    for expediente in expedientes:
        codigo = expediente % 10  
        if codigo in buzones:
            buzon = buzones[str(codigo)]
            if buzon not in asignaciones:
                asignaciones[buzon] = []
            asignaciones[buzon].append(expediente)
    return asignaciones


expedientes = [123, 456, 789, 101, 112, 223, 334, 445, 556, 667, 778, 889, 990]
asignaciones = asignar_expedientes(expedientes)

for buzon, expedientes_asignados in asignaciones.items():
    print(f"Expedientes en buzón {buzon}: {expedientes_asignados}")