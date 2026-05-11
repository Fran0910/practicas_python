lista_alumnos=[]

for numero in range(1,6):
    nombre=input("Ingrese el nombre: ")
    apellidos=input("Ingrese los apellidos: ")
    persona={
        "nombre":{nombre},
        "apellidos":{apellidos}
    }

lista_alumnos.append(persona)