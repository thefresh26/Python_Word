#Encapsulacion

class Cliente:
    def __init__(self):
        self.__codigo = 4321

#El proceso de cambiar del nombre del atributo se llama mangling

class cliente:
    def __init__(self):
        self.__codigo = 4321
    
    def __cuenta(self):
        return 'Cuenta de procesamiento'

    def getcodigo(self):
        return self.__codigo

r = cliente()
print(r._cliente__codigo)
r._cliente__cuenta()

    
