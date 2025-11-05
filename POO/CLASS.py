 #Las clases:
 
class Equipo:
    print("Bienvenido a los jugadores\n")
    j1 = "ronaldiño"
    j2 = "falcao"
    print(f"{j1}: 1")
    print(f"{j2}: 2")
    
    valor = int(input("¿Que jugador desea seleccionar?: "))
    if valor == 1:
        print(f"Usted ha seleccionado a: {j1}")
    if valor == 2:
        print(f"Usted ha seleccionado a: {j2}")
        
Equipo()
print()

class nombre:
    pass

victor = nombre()
maria = nombre()

victor.edad = 30
victor.sexo = "Maculino"
victor.pais = "Bolivia"

maria.edad = 25
maria.sexo = "Femenino"
maria.pais = "colombia"

print(f"La edad de victor es: {victor.edad}")