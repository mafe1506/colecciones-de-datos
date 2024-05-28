alumnos = []


while True:
    nombre = input("Introduce el nombre del alumno (o '*' para terminar): ")


    if nombre == '*':
        break

    edad = int(input("Introduce la edad del alumno: "))


    alumnos.append((nombre, edad))


print("Estudiantes mayores de edad:")
for alumno in alumnos:
    if alumno[1] >= 18:
        print(f"{alumno[0]} - {alumno[1]} años")


edad_maxima = max(alumnos, key=lambda x: x[1])[1]


print("\nAlumnos mayores:")
for alumno in alumnos:
    if alumno[1] == edad_maxima:
        print(f"{alumno[0]} - {alumno[1]} años")