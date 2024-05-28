dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


numero_mes = int(input("Ingresa el número de mes (1-12): "))


if numero_mes < 1 or numero_mes > 12:
    print("Número de mes inválido.")
else:
    dias_del_mes = dias_por_mes[numero_mes - 1]

    nombres_meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    nombre_mes = nombres_meses[numero_mes - 1]

    print(f"El mes de {nombre_mes} tiene {dias_del_mes} días.")