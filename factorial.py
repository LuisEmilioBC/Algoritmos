def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def main():
    try:
        numero=int(input("Ingrese un número para calcular su factorial: "))
        if numero < 0:
            print("No se puede calcular con números negativos")
        else:
            resultado=factorial(numero)
            print(f"El factorial de {numero} es {resultado}")
    except ValueError:
        print("Se debe ingresar un número entero válido")

main()