import numpy as np

def put_one_in_None(plate):
    for i in range(len(plate)):
        for j in range(len(plate[0])):
            if plate[i][j] == None:
                plate[i][j] = float(1)
    return plate

def gauss_seidel(plate, epsilon=1e-6, maxiter=100):
    equal = plate[-1].copy()
    new_equal = equal.copy()
    old_equal = []
    plate.pop(-1)
    diag = np.diag(plate)
    res = epsilon + 1  # Inicializar res com um valor maior que epsilon
    itera = 0

    while (epsilon < res or itera < maxiter):
        for i in range(len(equal)):
            new_equal.append(((equal[i] + sum(plate[i])) / diag[i]))

        res = np.max(np.abs(np.array(new_equal) - np.array(old_equal)))
        itera += 1
        old_equal = new_equal
        new_equal = []  # Redefinir new_equal a cada iteração

    print("Iterações:", itera)
    print("Aproximação:", res)
    return new_equal
