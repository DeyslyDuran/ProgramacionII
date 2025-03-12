class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def tamano(self):
        return len(self.elementos)

    def frente(self):
        if not self.esta_vacia():
            return self.elementos[0]
        else:
            raise IndexError("La cola está vacía")
class CribaDeEratostenes:
    def __init__(self, max_num):
        self.max_num = max_num
        self.lista_primos = self._criba_de_eratostenes()

    def _criba_de_eratostenes(self):
        primos = [True] * (self.max_num + 1)
        p = 2
        while (p * p <= self.max_num):
            if primos[p]:
                for i in range(p * p, self.max_num + 1, p):
                    primos[i] = False
            p += 1
        return [p for p in range(2, self.max_num + 1) if primos[p]]

    def es_primo(self, num):
        return num in self.lista_primos
# Crear la cola A y añadir los números
A = Cola()
A.encolar(11)
A.encolar(10)
A.encolar(5)
A.encolar(22)

# Encontrar el número máximo en la cola A
max_num = max(A.elementos)

# Crear una instancia de la clase CribaDeEratostenes
criba = CribaDeEratostenes(max_num)

# Crear las colas B y C para primos y no primos
B = Cola()
C = Cola()

# Separar los números de A en B (primos) y C (no primos)
while not A.esta_vacia():
    num = A.desencolar()
    if criba.es_primo(num):
        B.encolar(num)
    else:
        C.encolar(num)

# Mostrar los resultados
print("Cola B (primos):", B.elementos)  # Salida: [11, 5]
print("Cola C (no primos):", C.elementos)  # Salida: [10, 22]
