resultado = 0 
print ("elija una entre divicion, multiplicasion, suma o resta")
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))
def suma():
    a+b
    resultado=a+b
    return(resultado)
def resta():
    a-b
    resultado=a-b
    return(resultado)
print("El resultado de la suma es: ")
print(a+b)
print("EL resultado de la resta es: ")
print(a-b)

resultado = 0 
print ("elija una entre divicion y multiplicasion")
def divicion ():
 a = int (input ("escribe el primer numero "))
 b = int (input ("escribe el segudo numero"))
 resultado = a/b
 return (resultado)

def multiplicasion ():
 a = int (input ("escribe el primer numero"))
 b = int (input ("escribe el segundo numero"))
 resultado = a * b
 return (resultado)


if __name__ == "__main__":
    print("Suma:", suma(10, 5))
    print("Resta:", resta(10, 5))
