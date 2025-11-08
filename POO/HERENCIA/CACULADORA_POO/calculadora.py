from main import inicio

inicio()

class Calculadora(inicio):
    
    print("[1]suma")
    print("[2]resta")
    print("[3]multiplicacion")
    print("[4]division")
    
    op = int(input("Que opcion desea realizar: "))
    
    match op:
            
        case 1: 
            def suma(self):
                suma = self.n1 + self.n2
                return 'La suma es: {}'.format(suma)
                print(suma)
            
        case 2:
            def resta(self):
                resta = self.n1 - self.n2
                return 'La resta es: {}'.format(resta)
        
        case 3:
            def resta(self):
                multiplicacion = self.n1 * self.n2
                return 'La resta es: {}'.format(multiplicacion)
            
        case 4:
            def resta(self):
                division = self.n1 // self.n2
                return 'La resta es: {}'.format(division)


 