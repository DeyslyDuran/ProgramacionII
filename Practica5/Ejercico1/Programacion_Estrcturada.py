import math

def getDiscriminante(a, b, c):
    return b**2 - 4*a*c

def getRaiz1(a, b, discriminante):
    return (-b + math.sqrt(discriminante)) / (2 * a)

def getRaiz2(a, b, discriminante):
    return (-b - math.sqrt(discriminante)) / (2 * a)

def main():
    # Solicitar al usuario que ingrese los valores de a, b y c
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    
    discriminante = getDiscriminante(a, b, c)
    
    if discriminante > 0:
        r1 = getRaiz1(a, b, discriminante)
        r2 = getRaiz2(a, b, discriminante)
        print(f"La ecuación tiene dos raíces: {r1:.5f} y {r2:.5f}")
    elif discriminante == 0:
        r1 = -b / (2 * a)
        print(f"La ecuación tiene una raíz: {r1}")
    else:
        print("La ecuación no tiene raíces reales")

if __name__ == "__main__":
    main()
