#Polimorfismo con funcion

class pera:
    def tipo(self):
        return 'fruta'

    def color(self):
        return "amarillo"
    
class lechuga:
    def tipo(self):
        return 'vegetal'

    def color(self):
        return "Verde"
    
def funcion(objeto): #es util para guardar los metodos de diferentes clases
    objeto.tipo()
    objeto.color()

nuevo_topmate = pera()
funcion(nuevo_topmate)


    