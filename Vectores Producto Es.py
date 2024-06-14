import numpy as np
import matplotlib.pyplot as plt

# Definición de vectores
u = np.array([1, 2])
v = np.array([3, 4])

# Producto escalar de los vectores
dot_product = np.dot(u, v)
print(f"El producto escalar de {u} y {v} es {dot_product}")

# Gráfica de los vectores
fig, ax = plt.subplots()
ax.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r', label='u')
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='g', label='v')

# Configuración del gráfico
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.grid(True)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.set_aspect('equal')
plt.legend()
plt.title('Vectores u y v')
plt.show()
