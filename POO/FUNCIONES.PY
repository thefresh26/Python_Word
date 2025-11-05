
try:
    class Persona:
        edad = 27
        nombre = "victor"
        pais = "brazil"

    doctor = Persona()
    print(doctor.edad)
    print(f"La edad es: {getattr(doctor,'edad')}") #manera directa
    print(f"¿El doctor tiene una edad?: {hasattr(doctor,'edad')}") #si existe o no

    print(f"Antes: {doctor.nombre}")
    setattr(doctor, 'nombre', 'Hector')
    print(f"Despues: {doctor.nombre}")

    delattr(Persona, 'pais') # borra un atributo
    print(doctor.pais)

except AttributeError:
    print("Already no Exist")
    