#polimorfismo con Herencia

class aves:
    def volar(self):
        return 'Algunas aves vuelan'
    
class aguila(aves):
    def volar(self):
        return 'Aguilla: si'
    
class gallina(aves):
    def volar(self):
        return 'Gallina: no'
    
#obtener clases
p = aves()
aguila = aguila()
gallina = gallina()

#impresiones
print(f'{p.volar()} Como:')
print(f'Aves: \n{aguila.volar()}')
print(gallina.volar())