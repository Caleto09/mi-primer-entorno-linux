# Caleb Raya 04/12/26
# Try It Yourself 2-3 a 2-8
nombre = "Caleb"
print(f"Hola {nombre}, ¿te gustaría aprender Python hoy?")
# Name Cases:
nombre = "Caleb de Jesús raya mendoza"
print(f"{nombre.title()}\n{nombre.upper()}\n{nombre.lower()}")
# Famous Quote:
autor = "Albert Einsten"
quote = "A person who never made a mistake never tried anything new"
print(f'{autor} once said, "{quote}".')
# Stripping Names:
name = "   Elías \t\nSamuel \tGonzalo \nBocanegra.     "
print(name)
print(f"{name.lstrip()},\n{name.rstrip()},\n{name.strip()}")
# File Extensions:
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
