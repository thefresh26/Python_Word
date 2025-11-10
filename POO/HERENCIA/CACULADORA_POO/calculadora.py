
class Calculadora():

    def vizulizar(self,n1 ,n2):
        
        print("[1]SUMA")
        print("[2]RESTA")
        print("[3]MULTIPLICACION")
        print("[4]DIVISION")
        op = int(input("Ingrese la opcion que desea realizar: "))
        
        match op:
            
            case 1:
                suma = n1 + n2
                return 'La suma total es: {}'.format(suma)
            
            case 2:
                resta = n1 - n2
                return 'La resta total es: {}'.format(resta)
            
            case 3:
                multiplicacion = n1 * n2
                return 'La mulitplicacion total es: {}'.format(multiplicacion)
            
            case 4:
                division = n1 // n2
                return 'La division  total es: {}'.format(division)
                
        

 