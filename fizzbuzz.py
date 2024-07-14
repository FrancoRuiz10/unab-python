#numero es multiplo de 3 -> fizz
#numero es multiplo de 5 -> buzz
#si el numero es multiplo de 5 y ademas de 3->fizzbuzz
#si no es multiplo de 3 o de 5 ->numero

for numero in range(0,50):
    if  (numero % 3 == 0) and (numero % 5 == 0):
        print("FizzBuzz")
    elif numero%3==0:
        print("Fizz")
    elif numero%5==0:
        print("Buzz")
    else:
        print(numero)

