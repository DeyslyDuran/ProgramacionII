import matplotlib.pyplot as plt
import numpy as np
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return [self.x, self.y]

    def coord_polares(self):
        radio = math.sqrt(self.x**2 + self.y**2)
        angulo = math.atan2(self.y, self.x)
        angulo = math.degrees(angulo)
        return [radio, angulo]

    def __str__(self):
        return f"Punto:({self.x:.2f}, {self.y:.2f})"

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __str__(self):
        return f"Línea de {self.p1} a {self.p2}"

    def dibuja_linea(self):
        plt.plot([self.p1.x, self.p2.x], [self.p2.y, self.p2.y], 'ro-')

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio {self.radio:.2f}"

    def dibuja_circulo(self):
        circle = plt.Circle((self.centro.x, self.centro.y), self.radio, fill=False, color='b')
        plt.gca().add_patch(circle)

def main():
    # Crear y mostrar la ventana para los gráficos
    punto = Punto(230, 230)
    print(punto)
    print("Coordenadas cartesianas:",punto.coord_cartesianas())
    print("Coordenadas polares:",punto.coord_polares())

    # Dibujar la linea
    linea = Linea(punto, Punto(130, 230))
    print(linea)
    linea.dibuja_linea()

    # Dibujar el circulo
    circulo = Circulo(punto, 100)
    print(circulo)
    circulo.dibuja_circulo()

    # Configurar y mostrar la grafica
    plt.xlim(0, 500)
    plt.ylim(0, 500)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Grafico de Linea y Circulo')
    plt.show()

if __name__ == "__main__":
    main()
