#metodo constructor

class Persona:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    
    def descripcion(self):
        return 'nombre: {} tiene {} años'.format(self.nombre, self.año)
    
    def comentario(self, comentario):
        return ''.format(self.nombre, comentario)

        
        
    
        