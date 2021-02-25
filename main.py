# Entradas
numero = int(input("Introduce un número: "))

# Proceso
if numero % 10 == 0:
    resultado = "sí"
else:
    resultado = "no"

# Salidas
print("El número", numero, resultado, "es divisible entre 10")
