import numpy as np
import matplotlib.pyplot as plt

# Definición de vectores
u = np.array([1, 2])
v = np.array([3, 1])

# Suma de vectores
w = u + v

# Producto por un escalar
alpha = 2
u_scaled = alpha * u

# Gráfica de los vectores
plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r', label='u')
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='g', label='v')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b', label='u + v')
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid()
plt.legend()
plt.show()
