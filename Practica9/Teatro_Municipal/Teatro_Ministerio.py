import tkinter as tk
from tkinter import messagebox

# Clases de boletos
class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.precio = 50.0 if dias_anticipacion >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.precio = 25.0 if dias_anticipacion >= 10 else 30.0


# Interfaz gráfica con Tkinter
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")

        # Título
        tk.Label(root, text="Teatro Municipal", font=("Arial", 20)).pack(pady=10)

        # Tipo de boleto
        self.tipo_boleto = tk.StringVar(value="Palco")
        frame_tipos = tk.Frame(root)
        tk.Label(frame_tipos, text="Datos del Boleto").pack()
        tk.Radiobutton(frame_tipos, text="Palco", variable=self.tipo_boleto, value="Palco").pack(side=tk.LEFT)
        tk.Radiobutton(frame_tipos, text="Platea", variable=self.tipo_boleto, value="Platea").pack(side=tk.LEFT)
        tk.Radiobutton(frame_tipos, text="Galería", variable=self.tipo_boleto, value="Galeria").pack(side=tk.LEFT)
        frame_tipos.pack(pady=5)

        # Número y días
        frame_datos = tk.Frame(root)
        tk.Label(frame_datos, text="Número:").grid(row=0, column=0)
        self.txt_numero = tk.Entry(frame_datos, width=20)
        self.txt_numero.grid(row=0, column=1)

        tk.Label(frame_datos, text="Cant. Días para el Evento:").grid(row=1, column=0)
        self.txt_dias = tk.Entry(frame_datos, width=20)
        self.txt_dias.grid(row=1, column=1)
        frame_datos.pack(pady=20)

        # Botones
        frame_botones = tk.Frame(root)
        tk.Button(frame_botones, text="Vende", command=self.vender_boleto).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botones, text="Salir", command=root.quit).pack(side=tk.LEFT, padx=10)
        frame_botones.pack(pady=20)

        # Resultado
        self.lbl_info = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.lbl_info.pack(pady=40)

    def vender_boleto(self):
        try:
            numero = int(self.txt_numero.get())
            tipo = self.tipo_boleto.get()

            dias = 0
            if tipo in ["Platea", "Galeria"]:
                dias = int(self.txt_dias.get())

            if tipo == "Palco":
                boleto = Palco(numero)
            elif tipo == "Platea":
                boleto = Platea(numero, dias)
            else:
                boleto = Galeria(numero, dias)

            self.lbl_info.config(text=str(boleto))

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()