import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self, discriminante):
        return (-self.b + math.sqrt(discriminante)) / (2 * self.a)

    def getRaiz2(self, discriminante):
        return (-self.b - math.sqrt(discriminante)) / (2 * self.a)

    def resolver(self):
        discriminante = self.getDiscriminante()
        
        if discriminante > 0:
            r1 = self.getRaiz1(discriminante)
            r2 = self.getRaiz2(discriminante)
            return f"La ecuación tiene dos raíces: {r1:.5f} y {r2:.5f}"
        elif discriminante == 0:
            r = -self.b / (2 * self.a)
            return f"La ecuación tiene una raíz: {r}"
        else:
            return "La ecuación no tiene raíces reales"

def main():
    # Solicitar al usuario que ingrese los valores de a, b y c
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    
    ecuacion = EcuacionCuadratica(a, b, c)
    resultado = ecuacion.resolver()
    print(resultado)

if __name__ == "__main__":
    main()
