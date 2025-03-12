class Pila:
    def __init__(self):
        self.arreglo = []
    def push(self,e):
        self.arreglo.append(e)
    def pop (self):
        e = -1 
        if not self.isEmpty ():
            e = self.arreglo()
        else:
            print("intenta sacar ")
        return e
    def peek (self):
        e = -1
        if not self.isEmpty():
            n= len(self.arreglo)
            e = self.arreglo[n-1]
        else:
            print ("intenta obtener un ")
        return e
    def isEmpty(self):
        return len (self.arreglo)==0
A = Pila ()
A.push(13)
A.push(22)
A.push(7)
B = Pila()#pares
C = Pila()#impares
while not A.isEmpty():
    e = A.pop()
    if e % 2 ==0 :
        B.push(e)
    else:
        C.push(e)
print("b....")
while not B.isEmpty():
    print(B.pop())
print("c....")
while not C.isEmpty():
    print(C.pop())



