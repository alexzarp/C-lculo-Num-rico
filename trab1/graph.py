import matplotlib.pyplot as plt
import numpy as np

def plot_3d_graph(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Criar as coordenadas X e Y da malha
    x = np.arange(0, cols, 1)
    y = np.arange(0, rows, 1)
    X, Y = np.meshgrid(x, y)

    # Converter a matriz para o tipo float e substituir os valores None por np.nan
    Z = np.array(matrix, dtype=float)
    Z[Z == None] = np.nan

    # Obter os valores de temperatura excluindo os np.nan
    temperatures = Z[~np.isnan(Z)]

    # Calcular o mínimo e o máximo das temperaturas
    min_temp = np.nanmin(temperatures)
    max_temp = np.nanmax(temperatures)

    # Definir as cores com base nas temperaturas usando o colormap 'coolwarm'
    cmap = plt.cm.get_cmap('inferno')
    norm = plt.Normalize(min_temp, max_temp)
    colors = cmap(norm(Z))

    # Criar a figura e o eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotar a superfície 3D com shading suave
    ax.plot_surface(X, Y, Z, facecolors=colors, rstride=1, cstride=1)

    # Configurar o mapa de cores
    mappable = plt.cm.ScalarMappable(cmap=cmap)
    mappable.set_array(temperatures)
    plt.colorbar(mappable)

    # Configurar os rótulos dos eixos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Temperatura')

    # Exibir o gráfico
    plt.show()