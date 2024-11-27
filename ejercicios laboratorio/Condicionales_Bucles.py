# Determinar si un número es par o impar utilizando condicionales
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Iterar sobre una lista de números e imprimir sus cuadrados utilizando un bucle for
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

# Solicitar repetidamente la entrada del usuario hasta que se cumpla una condición específica utilizando un bucle while
while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada.lower() == 'salir':
        break
