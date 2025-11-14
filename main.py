# main.py - Simulador 2D de fluidos
import numpy as np
import matplotlib.pyplot as plt

N = 50
u = np.zeros((N, N))
v = np.zeros((N, N))

# Obstáculo circular
for i in range(N):
    for j in range(N):
        if (i-25)**2 + (j-35)**2 < 36:
            u[i,j] = v[i,j] = 0

# Simulación
for step in range(200):
    un = u.copy()
    u[1:-1,1:-1] = un[1:-1,1:-1] + 0.01 * (
        -un[1:-1,1:-1]*(un[1:-1,1:-1]-un[0:-2,1:-1])
        + 0.1*(un[2:,1:-1] + un[0:-2,1:-1] + un[1:-1,2:] + un[1:-1,0:-2] - 4*un[1:-1,1:-1])
    )
    if step % 20 == 0:
        plt.clf()
        x, y = np.meshgrid(range(N), range(N))
        plt.quiver(x, y, u, v, scale=20)
        plt.title(f"Flujo 2D - Paso {step}")
        plt.pause(0.01)

plt.show()

Add simulador de fluidos
