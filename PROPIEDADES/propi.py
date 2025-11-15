#Propiedades

class empleado:
    def __init__(self, cliente, ingresos):
        self.__cliente = cliente
        self.__ingresos = ingresos
        
    #GET
    def __getcliente(self):
        return self.__cliente
    def __getingresos(self):
        return self.__ingresos
    
    #SET
    def __setcliente(self,cliente):
        self.__cliente = cliente
    def __setingresos(self,ingresos):
        self.__ingresos = ingresos
    
    #DEL 
    def __delcliente(self):
        del self.__cliente
    def __delingresos(self):
        del self.__ingresos

    cliente = property(fget= __getcliente,
                       fset= __setcliente,
                       fdel= __delcliente,
                       
                       doc= f'Soy el cliente')
    
    ingreso = property(fget= __getingresos)
    

cliente = empleado('juan',2000)
ingreso = empleado('juan',2000)
print(ingreso.ingreso)
