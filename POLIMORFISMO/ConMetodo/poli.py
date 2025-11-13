#Polimorfismo con metodo

class perro:
    def accion(self):
        self.perro_hace = 'GUAU'
        return f'El perro hace: {self.perro_hace}'
    
    def tipo_animal(self):
        return 'El Perro es: Domestico'
    
    
class gato:
    def accion(self):
        self.gato_hace = 'MIAU'
        return f'El gato hace: {self.gato_hace}'
    
    def tipo_animal(self):
        return 'El Gato es: Domestico'
    

a1 = perro()
a2 = gato()

print(f'Caracteristicas Perro:')
print(a1.accion())
print(a1.tipo_animal())

print()

print(f'Caracteristicas Gato:')
print(a2.accion())
print(a2.tipo_animal())