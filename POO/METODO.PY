class Matematica:
    def suma(self):
        
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(f"Promedio es: {(s.n1+s.n2)/2}")

class Ropa:
    def __init__(self):
        self.marca = "willow"
        self.talla = "M"
        self.color = "rojo"

camisa = Ropa()
print(f"El color de la camisa es: {camisa.color}")
print()


while True:
    class Calculadora:
        def __init__(self):
            
            self.n1 = int(input("Ingrese el numero 1: "))
            self.n2 = int(input("Ingrese el numero 2: "))
                    
            print("[1] Suma")
            print("[2] Resta")
            print("[3] Multiplicacion")
            print("[4] Division")
            
            op = int(input("¿Que quiere realizar?"))
            match op:
                case 1:
                    self.suma = self.n1 + self.n2
                    print(f" La suma es: {self.suma}")
                    
                case 2:
                    self.resta = self.n1 - self.n2
                    print(f" La resta es: {self.resta}")
                    
                case 3:
                    self.multiplicacion = self.n1 * self.n2
                    print(f" La multiplicacion es: {self.multiplicacion}")
                        
                case 4:
                    self.division = self.n1 // self.n2
                    print(f" La division es: {self.division}")
                    
    operacion = Calculadora()
    
    
    again = input("¿Desea Salir? (S/N)").lower()
    if again == "s":
        break                            


        
        
        