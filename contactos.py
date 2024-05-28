def agregar_contacto(libreta, nombre, telefono):
    libreta.append((nombre, telefono))
    print(f"Contacto {nombre} agregado correctamente.")

def buscar_contacto(libreta, nombre):
    for contacto in libreta:
        if contacto[0] == nombre:
            return contacto
    return None

def listar_contactos(libreta):
    if not libreta:
        print("La libreta está vacía.")
    else:
        print("Lista de contactos:")
        for contacto in libreta:
            print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

libreta_contactos = []

agregar_contacto(libreta_contactos, "Juan", "3045679843")
agregar_contacto(libreta_contactos, "María", "3007654578")
agregar_contacto(libreta_contactos, "Pedro", "3025890911")


listar_contactos(libreta_contactos)

nombre_buscar = input("Ingrese el nombre del contacto que desea buscar: ")
contacto_encontrado = buscar_contacto(libreta_contactos, nombre_buscar)
if contacto_encontrado:
    print(f"Contacto encontrado - Nombre: {contacto_encontrado[0]}, Teléfono: {contacto_encontrado[1]}")
else:
    print("El contacto no se encontró.")

nombre_nuevo = input("Ingrese el nombre del nuevo contacto: ")
telefono_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
agregar_contacto(libreta_contactos, nombre_nuevo, telefono_nuevo)

listar_contactos(libreta_contactos)