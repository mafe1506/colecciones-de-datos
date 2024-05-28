def alumno_con_promedio_mas_alto(alumnos):
    mejor_promedio = 0
    mejor_alumno = None
    for alumno in alumnos:
        nombre, edad, promedio = alumno
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = alumno
    return mejor_alumno

def mostrar_alumno(alumno):
    nombre, edad, promedio = alumno
    print(f"Nombre: {nombre}, Edad: {edad}, Promedio: {promedio}")

alumnos = [
    ("Juan", 20, 8.5),
    ("María", 21, 9.2),
    ("Pedro", 19, 7.8),
    ("Ana", 22, 8.9)
]

print("Información de todos los alumnos:")
for alumno in alumnos:
    mostrar_alumno(alumno)

mejor_alumno = alumno_con_promedio_mas_alto(alumnos)
print("\nAlumno con el promedio más alto:")
mostrar_alumno(mejor_alumno)