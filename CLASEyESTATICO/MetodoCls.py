class pastel:
    def __init__(self, i1,i2):
        self.i1 = i1
        self.i2 = i2
        
    def __repr__(self):
        return (f'El pastel contiene: {self.i1 !r} Y el sabor es: {self.i2 }')
    
    @classmethod # cuando se trabaja con classmethod se utiliza con cls
    def Pastel_chocolate(cls):
        return cls('harina','chocolate')
    
    @classmethod
    def pastel_vainilla(cls):
        return cls(['harina','vainilla'])

print(pastel.Pastel_chocolate())