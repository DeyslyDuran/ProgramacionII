class Pila:
    def __init__(self, n):
        self.n = n
        self.arreglo = [None] * n
        self.top = -1

    def push(self, e):
        if not self.is_Full():
            self.top += 1
            self.arreglo[self.top] = e
        else:
            print("La pila está llena, no se puede agregar más elementos.")

    def pop(self):
        if not self.is_Empty():
            temp = self.arreglo[self.top]
            self.top -= 1
            return temp
        else:
            print("La pila está vacía, no se puede extraer elementos.")
            return None  

    def peek(self):
        if not self.is_Empty():
            return self.arreglo[self.top]
        else:
            print("La pila está vacía, no se puede obtener el elemento superior.")
            return None  

    def is_Empty(self):
        return self.top == -1

    def is_Full(self):
        return self.top == self.n - 1

    @staticmethod
    def main():
        pila = Pila(4)

        
        pila.push(13)
        pila.push(22)
        pila.push(7)

        
        print("Elemento superior:", pila.peek())

        
        print("Elemento retirado:", pila.pop())
        print("Elemento retirado:", pila.pop())

        
        print("¿La pila está vacía?", pila.is_Empty())

        
        print("¿La pila está llena?", pila.is_Full())


if __name__ == "__main__":
    Pila.main()
