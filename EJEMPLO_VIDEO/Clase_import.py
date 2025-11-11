from Clase_objeto import Calculadora

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2) # limitar los valores necesarios
        
    def suma(self):
        
        a,b, = self.datos
        s = a + b
        print(f"El resultado es: {s}")
    
    def resta(self):
        
        a,b, = self.datos
        r = a - b
        print(f"El resultado es: {r}")
        
        
class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
        
    def cuadrada(self):
        import math
        a, = self.datos
        print(f"El resultado es: {math.sqrt(a)}")
        