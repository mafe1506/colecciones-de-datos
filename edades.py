print("Ingresa las edades de las personas (ingresa '*' para terminar):")
edades = []

while True:
    edad = input("Edad (o '*' para terminar): ")


    if edad == '*':
        break

    try:
        edad = int(edad)
        edades.append(edad)
    except ValueError:
        print("Por favor, ingresa un número válido o '*' para terminar.")

edades.sort()

print("Edades ordenadas de menor a mayor:")
for edad in edades:
    print(edad)