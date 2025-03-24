import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros, promedio):
    varianza = sum((x - promedio) ** 2 for x in numeros) / (len(numeros) - 1)
    return math.sqrt(varianza)

def main():
    # Solicitar al usuario que ingrese 10 números
    numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))
    
    if len(numeros) != 10:
        print("Por favor, ingrese exactamente 10 números.")
        return
    
    prom = promedio(numeros)
    desv = desviacion(numeros, prom)
    
    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desv:.5f}")

if __name__ == "__main__":
    main()
