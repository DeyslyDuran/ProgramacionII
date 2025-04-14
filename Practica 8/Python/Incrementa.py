class A:
    def __init__ (self ,x,z):
        self.x=x
        self.z=z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1
    def incrementarZ(self):
        self.z += 1

    
        
class B:
    def __init__ (self,y,z):
        self.y=y
        self.z= z


    def incrementarYZ(self):
        self.y += 1
        self.z +=1

    def incrementarZ(self):
        self.z += 1

class D(A,B):
    def __init__ (self,x,y,z):
        A.__init__(self,x,z)
        B.__init__(self,y,z)

    def incrementarXYZ(self):
        self.x +=1
        self.y += 1
        self.z += 1

d = D(5, 10, 15)
print("Antes:")
#d.incrementaXZ()
#d.incrementarYZ()
print("x =", d.x, ", y =", d.y, ", z =", d.z)

print("Después de incrementaXYZ:")
d.incrementarXYZ()
print("x =", d.x, ", y =", d.y, ", z =", d.z)





   
