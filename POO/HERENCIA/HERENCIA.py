
class Pokemon:
    pass
    
    def Detalles(self):
        self.nombre = str(input("Ingrese el nombre del pokemon: "))

    def tipo(self):
        self.tipo = str(input("Ingrese el tipo de pokemon: "))
                
    def descripcion(self):
        return 'El pokemon: {} es de tipo: {}'.format(self.nombre,self.tipo)
    
