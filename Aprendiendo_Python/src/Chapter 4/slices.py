# Caleb Raya 07/01/26
# Try It Yourself 4-10 a 4-12

# Slices:
pizzas = ["salami", "tocino", "carnes frías", "pepperoni"]
for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}")
print("En serio amo la pizza!")

print(f"\nLos primeros tres elementos de la lista son: {pizzas[0:3]}")
print(f"Los tres elementos en el medio de la lista son: {pizzas[1:3]}")
print(f"Los últimos tres elementos de la lista son: {pizzas[-3:]}")

# My Pizzas, Your Pizzas:
pizzas = ["salami", "tocino", "carnes frías", "pepperoni"]
pizzas_amigo = pizzas[:]

pizzas.append("camarones")
pizzas_amigo.append("piña")

print("\nMis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza.title())

print("\nLas pizzas favoritas de mi amigo son:")
for pizza in pizzas_amigo:
    print(pizza.title())

# More Loops: este lo omití :P
