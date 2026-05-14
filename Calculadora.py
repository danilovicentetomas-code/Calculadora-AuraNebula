resultado = 0 
print ("elija una entre divicion , multiplicasion  (agregar suma y resta )")
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

resultado = 0 
print ("elija una entre divicion y multiplicasion")
def divicion ():
 a = int (input ("escrive el primer numero "))
 b = int (input ("escrive el segudo numero"))
 resultado = a/b
 return (resultado)

def multiplicasion ():
 a = int (input ("escrive el primer numero"))
 b = int (input ("escrive el segundo numero"))
 resultado = a * b
 return (resultado)


if __name__ == "__main__":
    print("Suma:", suma(10, 5))
    print("Resta:", resta(10, 5))
