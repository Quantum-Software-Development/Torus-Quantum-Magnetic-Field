
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Função para desenhar um Tesseract
def desenhar_tesseract(ax):
    # Pontos de um cubo em 3D
    pontos = np.array([[1, 1, 1],
                       [-1, 1, 1],
                       [-1, -1, 1],
                       [1, -1, 1],
                       [1, 1, -1],
                       [-1, 1, -1],
                       [-1, -1, -1],
                       [1, -1, -1]])

    # Linhas que conectam os pontos para formar um cubo
    linhas = [[pontos[i], pontos[j]] for i in range(len(pontos)) for j in range(i+1, len(pontos)) if np.sum(np.abs(pontos[i] - pontos[j])) == 2]

    # Desenhar cada linha do cubo
    for linha in linhas:
        ax.plot3D(*zip(*linha), color="b")

# Criar uma figura e um eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar o Tesseract
desenhar_tesseract(ax)

# Configurar os limites do eixo
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Mostrar o plot
plt.show()
