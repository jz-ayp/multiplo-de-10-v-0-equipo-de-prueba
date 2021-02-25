# Entradas
numero = int(input("Introduce un número: "))
#numero = int(input())

# Proceso
if numero % 10 == 0:
    resultado = "sí"
else:
    resultado = "no"

# Salidas
print("El número", numero, resultado, "es múltiplo de 10")
