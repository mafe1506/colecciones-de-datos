import random


numeros = [random.randint(1, 100) for _ in range(10)]

print("Lista original:", numeros)


numeros.sort()

print("Lista ordenada de menor a mayor:", numeros)