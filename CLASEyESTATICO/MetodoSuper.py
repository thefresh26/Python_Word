#metodo  super

class persona:
    def __init__(self, Nombre):
        print(f'La persona {Nombre} esta intentando arrancar el carro')
        print('Arranco...')

class persona_arranca_carro(persona):
    
    def __init__(self):
        print('La persona desea arrancar el carro')
        super().__init__('juan')# con la funcion super
        persona.__init__(self,'juan') # manual o con la clase
         
accion_persona = persona_arranca_carro()
print(accion_persona)

