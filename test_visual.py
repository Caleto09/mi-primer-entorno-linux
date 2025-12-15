import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = np.sin(x)

print(f"Éxito, estás usando pandas versión: {pd.__version__}")

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Seno de x', color='cyan')
plt.title("¡Bienvenido al Data Science en Linux!")
plt.legend()
plt.grid(True)
plt.show()