import numpy as np
import matplotlib.pyplot as plt

# Defina as funções
def f1(x):
    return x**2 - 5*x + 2

def f2(x):
    return x*np.exp(x) - 2

def f3(x):
    return np.exp(x) - 5*np.sin(x)

def f4(x):
    return x**3 - 3*x**2 - 5*x + 2

# Crie os arrays de x
x = np.linspace(-5, 5, 1000)

# Crie as figuras e os eixos
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

# Plote as funções em seus respectivos eixos
ax1.plot(x, f1(x))
ax2.plot(x, f2(x))
ax3.plot(x, f3(x))
ax4.plot(x, f4(x))

# Adicione rótulos aos eixos e títulos às figuras
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Gráfico de f(x) = x^2 - 5x + 2')

ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.set_title('Gráfico de f(x) = xe^x - 2')

ax3.set_xlabel('x')
ax3.set_ylabel('f(x)')
ax3.set_title('Gráfico de f(x) = e^x - 5sen(x)')

ax4.set_xlabel('x')
ax4.set_ylabel('f(x)')
ax4.set_title('Gráfico de f(x) = x^3 - 3x^2 - 5x + 2')

# Exiba as figuras
plt.show()
