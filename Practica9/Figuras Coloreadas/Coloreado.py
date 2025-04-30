import tkinter as tk
from tkinter import ttk
import random
import math
from abc import ABC, abstractmethod

# Interfaz Coloreado
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

# Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color: str):
        self.color = color

    def setColor(self, color: str):
        self.color = color

    def getColor(self) -> str:
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

# Cuadrado
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str):
        super().__init__(color)
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado

    def comoColorear(self) -> str:
        return "Colorear los cuatro lados"

    def _str_(self):
        return f"Cuadrado - Lado: {self.lado}, Color: {self.color}"

# Círculo
class Circulo(Figura):
    def __init__(self, radio: float, color: str):
        super().__init__(color)
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo - Radio: {self.radio}, Color: {self.color}"

# Función para generar colores aleatorios
def generar_color():
    colores = ["red", "green", "blue", "yellow", "black"]
    return random.choice(colores)

# Generar figuras aleatorias
def generar_figuras():
    figuras = []
    for _ in range(5):
        tipo = random.randint(1, 2)
        color = generar_color()
        if tipo == 1:
            lado = round(random.uniform(30, 80), 2)
            figura = Cuadrado(lado, color)
        else:
            radio = round(random.uniform(15, 40), 2)
            figura = Circulo(radio, color)
        figuras.append(figura)
    return figuras

# Aplicación gráfica
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Coloreadas")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, bg="white", width=500, height=500)
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Frame derecho con botón y resultados
        self.panel = tk.Frame(self)
        self.panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.boton = ttk.Button(self.panel, text="Generar Figuras", command=self.mostrar_figuras)
        self.boton.pack(pady=5)

        self.lista = tk.Text(self.panel, width=40, height=30)
        self.lista.pack()

    def mostrar_figuras(self):
        self.canvas.delete("all")
        self.lista.delete(1.0, tk.END)
        figuras = generar_figuras()

        x, y = 50, 50  # Posición inicial

        for figura in figuras:
            self.lista.insert(tk.END, f"{figura}\n")
            self.lista.insert(tk.END, f"Área: {figura.area():.2f}\n")
            self.lista.insert(tk.END, f"Perímetro: {figura.perimetro():.2f}\n")
            if isinstance(figura, Coloreado):
                self.lista.insert(tk.END, f"{figura.comoColorear()}\n")
            self.lista.insert(tk.END, "-"*40 + "\n")

            # Dibujar en el canvas
            color = figura.getColor()
            if isinstance(figura, Cuadrado):
                lado = figura.lado
                self.canvas.create_rectangle(x, y, x + lado, y + lado, fill=color)
                y += lado + 20
            elif isinstance(figura, Circulo):
                r = figura.radio
                self.canvas.create_oval(x, y, x + 2*r, y + 2*r, fill=color)
                y += 2*r + 20

# Ejecutar app
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()