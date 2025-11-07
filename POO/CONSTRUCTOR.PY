"""
#metodo constructor

class Persona:
    pass
    def __init__(self):
        self.nombre = str(input("Escriba su nombre: "))
        self.año = int(input("Escriba el año en que nacio: "))
    
    def descripcion(self):
        return 'nombre: {} tiene {} años'.format(self.nombre, self.año)
    
    def comentario(self, comentario):
        return ' La persona con nombre: {} dice: {}'.format(self.nombre, comentario)
    
doctor = Persona()

print(f"Su nombre es: {doctor.nombre} y nacio en: {doctor.año}")
print(f"{doctor.descripcion()}")
print(f"SR@; {doctor.comentario('PUTOS')}")
"""


class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    
    def descripcion(self):
        return 'nombre: {} tiene {} años'.format(self.nombre, self.año)
    
    def comentario(self, comentario):
        return ' La persona con nombre: {} dice: {}'.format(self.nombre, comentario)
    
doctor = Persona('JUAN', 2005)


print(f"Su nombre es: {doctor.nombre} y nacio en: {doctor.año}")
print(f"{doctor.descripcion()}")
print(f"SR@; {doctor.comentario('KKKK')}")



class Email:
    
    def __init__(self):
        self.enviado = False
        
    def enviar_correo(self):
        self.enviado = True
        
Estado = Email()
Estado.enviar_correo() #Se utiliza el otro metodo
print(Estado.enviado)



        
        
    
        