def es_palindromo(numero):
    numero_str = str(numero)
    return numero_str==numero_str[::-1]

numero=12
if es_palindromo(numero):
    print(f"{numero} es un palindromo")
else:
    print(f"{numero} no es palindromo")