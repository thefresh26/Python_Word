
#del se utiliza para limpiar recursos

class Smartphone:
    def __init__(self):
        pass
    
    def Telefono(self):
        print("Haciendo una llamada...")
        
    def Camara(self):
        pass
    
    def ReproduccionVideo(self):
        print("Reproduciendo un video...")

    def __del__(self):
        print("Telefono Apagado")

ver = Smartphone()
ver.Telefono()
