# Caleb Raya 06/01/26
# Try It Yourself 3-4 a 3-7

# Guest List:
invitados = ["mamá", "papá", "asa", "regina"]
print(f"Te invito a cenar {invitados[0].title()}")
print(f"Te invito a cenar {invitados[1].title()}")
print(f"Te invito a cenar {invitados[2].title()}")
print(f"Te invito a cenar {invitados[3].title()}")
print(invitados)

# Changing Guest List:
invitados[3] = "sayu"
print(invitados)

print(f"Te invito a cenar {invitados[0].title()}")
print(f"Te invito a cenar {invitados[1].title()}")
print(f"Te invito a cenar {invitados[2].title()}")
print(f"Te invito a cenar {invitados[3].title()}")
print(invitados)

# More Guests:
invitados.insert(0, "saúl")
invitados.insert(2, "carlo")
invitados.append("eric")
print(invitados)

print(f"Te invito a cenar {invitados[0].title()}")
print(f"Te invito a cenar {invitados[1].title()}")
print(f"Te invito a cenar {invitados[2].title()}")
print(f"Te invito a cenar {invitados[3].title()}")
print(f"Te invito a cenar {invitados[4].title()}")
print(f"Te invito a cenar {invitados[5].title()}")
print(f"Te invito a cenar {invitados[6].title()}")
print(invitados)

# Shrinking Guest List:
print(f"Lo siento mucho, no podré invitarte {invitados.pop(0).title()}")
print(f"Lo siento mucho, no podré invitarte {invitados.pop(1).title()}")
print(f"Lo siento mucho, no podré invitarte {invitados.pop(2).title()}")
print(f"Lo siento mucho, no podré invitarte {invitados.pop(2).title()}")
print(f"Lo siento mucho, no podré invitarte {invitados.pop(2).title()}")
print(f"Te invito a cenar {invitados[0].title()}")
print(f"Te invito a cenar {invitados[1].title()}")
del invitados[0]
del invitados[0]
print(invitados)
