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

calculate_tx_points(plate)

print_matrix_beautiful(plate,"Tx Points:")
print_matrix_beautiful(gauss_seidel(plate), "\nGauss-Seidel:") 

# plot_3d_graph(plate)