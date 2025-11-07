from HERENCIA import Pokemon


class PK1(Pokemon):

    def nombre_ataque(self):
        self.tipo_ataque = str(input("Ingrese el tipo de ataque que tiene: "))
        return 'Nombre: {} tipo_ataque: {}'.format(self.nombre, self.tipo_ataque)

pk1 = PK1()
pk1.Detalles()
print(pk1.nombre_ataque())


"""class PK2(Pokemon):
    
    def nombre_ataque(self, tipo_ataque):
        return 'Nombre: {} tipo_ataque: {}'.format(self.nombre, tipo_ataque)
""" 