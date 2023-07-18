# Usei esta tabela de base: http://www.tallesmello.com.br/wp-content/uploads/2019/08/KC-e-KS.pdf
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Dados de exemplo para X e Y
X = np.array([0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26])  # Valores de βx
Y = np.array([20.8, 10.5, 7.0, 5.3, 4.3, 3.6, 3.1, 2.8, 2.5, 2.2, 2.1, 1.9, 1.8])  # Valores correspondentes de Y C50

# Criação da função de interpolação
interp_func = interp1d(X, Y, kind='linear')  # Escolha o tipo de interpolação desejado

# Valor de βx para interpolação
beta_x = 0.26

# Exibição do valor de βx e o valor interpolado de Y
if beta_x < X[0] or beta_x > X[-1]:
    print("O valor de beta_x está fora do intervalo de interpolação.")
else:
    # Valor interpolado de Y para βx
    y_interpolated = interp_func(beta_x)
    print(f"Valor interpolado para beta_x={beta_x}: {y_interpolated}")

# Plotagem do gráfico
plt.plot(X, Y, 'o', label='Dados')
plt.plot(beta_x, y_interpolated, 'ro', label='Ponto interpolado')
plt.xlabel('βx')
plt.ylabel('Y')
plt.legend()
plt.show()
