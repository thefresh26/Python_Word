

class auto:
    def accion(self):
        self.estado = input("¿Desea arrancar?: ").lower()
        if self.estado == "s":
            print("Encendiendo...")
        elif self.estado == "n":
            print()    

class auto_dentener:
    def accion(self):
        self.estado = input("¿Desea detenerce?: ").lower()
        if self.estado == "s":
            print("Carro detenido...")
            
        else:
            print("Auto en movimiento...")


acciones_carro = [auto(),auto_dentener()]

for i in acciones_carro:
    i.accion()
