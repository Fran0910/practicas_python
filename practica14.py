equipos_lista = []
salida="no"

while salida != "fin":
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    equipos_lista.append(nombre_equipo)
    salida = input("Has terminado, introduzca fin para acabar: ")

print("Equipos introducidos: ")
print(equipos_lista)
print(len(equipos_lista))