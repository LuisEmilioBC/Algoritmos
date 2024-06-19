
lista = []
def secuencia_descendente(n):
    lista.append(n)
    if n>1:
        secuencia_descendente(n-1)
def main_secuencia_descendente():
    try:
        numero=int(input("Ingrese un número para calcular su secuencia hasta 1: "))
        if numero < 0:
            print("No se puede calcular con números negativos")
        else:
            secuencia_descendente(numero)
            print(f"La secuencia de {numero} hasta 1 es {lista}")
    except ValueError:
        print("Se debe ingresar un número entero válido")
main_secuencia_descendente()

lista1 = []
def secuencia_ascendente(n):
    if n>1:
        secuencia_ascendente(n-1)
    lista1.append(n)
def main_secuencia_ascendente():
    try:
        numero=int(input("Ingrese un número para calcular su secuencia desde 1: "))
        if numero < 0:
            print("No se puede calcular con números negativos")
        else:
            secuencia_ascendente(numero)
            print(f"La secuencia de {numero} desde 1 es {lista1}")
    except ValueError:
        print("Se debe ingresar un número entero válido")
main_secuencia_ascendente()


def palindromo(cadena):
    if len(cadena)<=1:
        return True
    elif cadena[0]==cadena[-1]:
        return palindromo(cadena[1:-1])
    else:
        return False
    
def main_palindromo():
    cadena=input("Ingrese una cadena para calcular si es palíndromo: ")
    if palindromo(cadena):
        print(f"La cadena '{cadena}' es un palíndromo")
    else:
        print(f"La cadena '{cadena}' NO es un palíndromo")
main_palindromo()


binario = []
def a_binario(n):
    if n != 0:
        digito = n%2
        a_binario(n//2)
        binario.append(str(digito)) 
        
def main_binario():
    try:
        numero=int(input("Ingrese un número para calcular su binario: "))
        if numero < 0:
            print("No se puede calcular con números negativos")
        else:
            a_binario(numero)
            print(f"El binario de {numero} es {''.join(binario)}")
    except ValueError:
        print("Se debe ingresar un número entero válido")
main_binario()       

