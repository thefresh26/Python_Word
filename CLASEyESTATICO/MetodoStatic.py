import math

class Pudin:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
        
    def __repr__(self):
        return f'Pudin({self.ingredientes} Y el tamaño es: {self.tamaño})'        
        
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi

nuevo_pastel = Pudin(['pan','harina','agua'],5)
print(f'El area del circulo es: {nuevo_pastel.tamaño_area(12)}')