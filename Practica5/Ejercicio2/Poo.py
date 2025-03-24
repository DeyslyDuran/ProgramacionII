import math

class Estadisticas:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        prom = self.promedio()
        varianza = sum((x - prom) ** 2 for x in self.numeros) / (len(self.numeros) - 1)
        return math.sqrt(varianza)

def main():
    # Solicitar al usuario que ingrese 10 números
    numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))
    
    if len(numeros) != 10:
        print("Por favor, ingrese exactamente 10 números.")
        return
    
    estadisticas = Estadisticas(numeros)
    prom = estadisticas.promedio()
    desv = estadisticas.desviacion()
    
    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desv:.5f}")

if __name__ == "__main__":
    main()
