import math
def mcm(num1, num2):
    return (num1*num2) // mcd(num1, num2)

def mcd(num1, num2):
   
    rest = 0
    while(num2 > 0):
        rest = num2
        num2 = num1 % num2
        num1 = rest
    return num1


def mostrar_menu():
    print("Operaciones matemáticas:")
    print("1. Suma.")
    print("2. Resta.")
    print("3. Multiplicación.")
    print("4. División.")
    print("5. Raíz Cuadrada.")
    print("6. Potenciación.")
    print("7. Mínimo Común Múltiplo (2 números).")
    print("8. Máximo Común Divisor (2 números.)")
    print("9. Salir")

def suma():
    print("Has seleccionado la Suma.")
    n1=float(input("Ingrese el primer número: "))
    n2=float(input("Ingrese el segundo número: "))
    res=n1+n2
    print("La respuesta es ", res)
    print(" ")
    n1=0
    n2=0
    res=0

def resta():
    print("Has seleccionado la Resta.")
    n1=float(input("Ingrese el primer número: "))
    n2=float(input("Ingrese el segundo número: "))
    res=n1-n2
    print("La respuesta es ", res)
    print(" ")
    n1=0
    n2=0
    res=0

def multiplicacion():
    print("Has seleccionado la Multiplicación.")
    n1=float(input("Ingrese el primer número: "))
    n2=float(input("Ingrese el segundo número: "))
    res=n1*n2
    print("La respuesta es ", res)
    print(" ")
    n1=0
    n2=0
    res=0

def division():
    print("Has seleccionado la División.")
    n1=float(input("Ingrese el primer número: "))
    n2=float(input("Ingrese el segundo número: "))
    res=n1/n2
    print("La respuesta es ", res)
    print(" ")
    n1=0
    n2=0
    res=0

def raiz():
    print("Has seleccionado la Raíz Cuadrada.")
    n1=float(input("Ingrese el primer número: "))
    res=math.sqrt(n1)
    print("La respuesta es ", res)
    print(" ")
    n1=0
    res=0
    


def potenciación():
    print("Has seleccionado la Potenciación.")
    n1=float(input("Ingrese el número: "))
    n2=float(input("Ingrese el exponente: "))
    res=n1**n2
    print("La respuesta es ", res)
    print(" ")
    n1=0
    n2=0
    res=0


def mcm1():
    print("Has seleccionado la Mínimo Común Múltiplo (2 números).")
    num1=float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo número: "))
    res=mcm(num1,num2)
    print("La respuesta es ", res)
    print(" ")
    num1=0
    num2=0
    res=0


def mcd1():
    print("Has seleccionado la Máximo Común Divisor (2 números.).")
    num1=float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo número: "))
    res=mcd(num1, num2)
    print("La respuesta es ", res)
    print(" ")
    num1=0
    num2=0
    res=0
    
    

def prg():
    while True:
        mostrar_menu()
        opcion = input("Bienvenido, ingrese la opción que desee: ")

        if opcion == "1":
            suma()
        elif opcion == "2":
            resta()
        elif opcion == "3":
            multiplicacion()
        elif opcion == "4":
            division()
        elif opcion == "5":
            raiz()
        elif opcion == "6":
            potenciación()
        elif opcion == "7":
            mcm1()
        elif opcion == "8":
            mcd1()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    prg()
