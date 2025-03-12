import math

class AreaCalculator:
    def calcular_area(self, figura, *args):
        if figura == "circulo":
            return self._area_circulo(*args)
        elif figura == "rectangulo":
            return self._area_rectangulo(*args)
        elif figura == "triangulo":
            return self._area_triangulo(*args)
        elif figura == "cuadrado":
            return self._area_cuadrado(*args)
        elif figura == "trapecio":
            return self._area_trapecio(*args)
        elif figura == "pentagono":
            return self._area_pentagono(*args)
        else:
            return "Figura no reconocida"
    
    def _area_circulo(self, radio):
        return math.pi * radio ** 2
    
    def _area_rectangulo(self, largo, ancho):
        return largo * ancho
    
    def _area_triangulo(self, base, altura):
        return 0.5 * base * altura
    
    def _area_cuadrado(self, lado):
        return lado ** 2
    
    def _area_trapecio(self, base_mayor, base_menor, altura):
        return 0.5 * (base_mayor + base_menor) * altura
    
    def _area_pentagono(self, lado, apotema):
        return 0.5 * 5 * lado * apotema

# Ejemplos de uso
calculador = AreaCalculator()
print("Área del círculo (radio=5):", calculador.calcular_area("circulo", 5))
print("Área del rectángulo (largo=5, ancho=3):", calculador.calcular_area("rectangulo", 5, 3))
print("Área del triángulo (base=4, altura=2):", calculador.calcular_area("triangulo", 4, 2))
print("Área del cuadrado (lado=4):", calculador.calcular_area("cuadrado", 4))
print("Área del trapecio (base mayor=7, base menor=3, altura=4):", calculador.calcular_area("trapecio", 7, 3, 4))
print("Área del pentágono (lado=3, apotema=2.5):", calculador.calcular_area("pentagono", 3, 2.5))
