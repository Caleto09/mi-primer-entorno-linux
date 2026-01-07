# Caleb Raya 06/01/26
# Try It Yourself 4-3 a 4-9

# Counting to Twenty:
"""for valor in range(1, 21):
    print(valor)

 One Million:
un_millon = []
for valor in range(1, 1000001):
    un_millon.append(valor)
print(un_millon)"""

# Summing a Million:
"""print(min(un_millon))
print(max(un_millon))
print(sum(un_millon))"""

# Odd Numbers:
impares = []
for valor in range(1, 20, 2):
    impares.append(valor)
print(impares)

# Threes:
múltiplos = []
for valor in range(3, 31, 3):
    múltiplos.append(valor)
print(múltiplos)

# Cubes:
cubos = []
for valor in range(1, 11):
    cubos.append(valor**3)
print(cubos)

# Cube Comprehension:
cubos2 = [value**3 for value in range(1, 11)]
print(cubos2)
