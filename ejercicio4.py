def calcular_media():
    suma = 0
    contador = 0

    while True:
        try:
            numero = float(input("Ingresa un número positivo (0 para finalizar): "))
            if numero == 0:
                break
            elif numero < 0:
                print("Por favor, ingresa un número positivo.")
            else:
                suma += numero
                contador += 1
        except ValueError:
            print("Ingresa un valor numérico válido.")

    if contador > 0:
        media = suma / contador
        print(f"La media de los números ingresados es: {media:.2f}")
    else:
        print("No se ingresaron números válidos.")

calcular_media()
