def asignar_sala(numero_entrada):
    if numero_entrada==0:
        return "dirigete a la administracion para obtener una nueva entrada"
    elif numero_entrada %2 ==0:
        return "dirigete a la sala 1"
    else:
        return "dirigete a la sala 2"

entradas=[123,456,789,101,112,223,334,446,665,998,885,0]
for entrada in entradas:
    print(f"Para la entrada {entrada}: {asignar_sala(entrada) }")
