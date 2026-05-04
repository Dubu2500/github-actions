from datetime import datetime

a = 15
b = 25

print("Iniciando script Python...")
print(f"La suma de {a} + {b} = {a + b}")
print(f"La multiplicacion de {a} x {b} = {a * b}")

fecha = datetime.now().strftime("%d de %B de %Y")
print(f"Fecha de ejecucion: {fecha}")
print("Script finalizado correctamente.")
