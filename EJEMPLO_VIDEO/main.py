from Clase_objeto import Calculadora
from Clase_import import op_basicas, raiz

"""vizualizar = op_basicas()
vizualizar.ingresar_datos()
vizualizar.suma()"""

objeto = op_basicas()
print(isinstance(objeto, op_basicas)) # si esta trabajando con la funcion indicada
print(issubclass(op_basicas, Calculadora)) # trabaja con la subclases, praticamente las que se importan



#hay que ser organizados al momento de imprimir