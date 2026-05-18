def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error: división entre cero"
    return a / b

def multiplicacion(a, b):
    return a * b

# Menú
print("Elija una operación: suma, resta, division o multiplicacion")
operacion = input("Operación: ").lower()

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if operacion == "suma":
    print("Resultado:", suma(a, b))
elif operacion == "resta":
    print("Resultado:", resta(a, b))
elif operacion == "division":
    print("Resultado:", division(a, b))
elif operacion == "multiplicacion":
    print("Resultado:", multiplicacion(a, b))
else:
    print("Operación no válida")
