
class Calculadora:
    
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
        
    def ingresar_datos(self):
            self.datos = [int(input('ingresar dato: ' + str(i+1) + ' = ')) for i in range(self.n)]
    
    
        
