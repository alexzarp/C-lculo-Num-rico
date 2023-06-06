from functions import *
from gaussSeidel import *
from graph import *  

plate = [
    [None, 25, 30, None, None],
    [70, 't1', 't2', 20, None],
    [80, 't3', 't4', 't5', 10],
    [100, 't6', 't7', 't8', 15],
    [None, 90, 110, 120, None]
]

mat = [
    [4, -1, -1, 0, 0, 0, 0, 0],
    [-1, 4, -1, 0, -1, 0, 0, 0],
    [-1, -1, 4, 0, 0, -1, 0, 0],
    [0, 0, 0, 4, -1, -1, 0, -1],
    [0, -1, 0, -1, 4, 0, -1, 0],
    [0, 0, -1, -1, 0, 4, -1, 0],
    [0, 0, 0, 0, -1, -1, 4, -1],
    [0, 0, 0, -1, 0, 0, -1, 4],
    [95, 50, 80, 0, 30, 190, 110, 125]
]


calculate_tx_points(plate)

print_matrix_beautiful(plate,"Tx Points:")
print_matrix(gauss_seidel(mat), "\nGauss-Seidel:") 

plot_3d_graph(mat)