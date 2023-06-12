import numpy as np

def jacobi_method(plate, epsilon=1e-6, maxiter=100):
    equal = plate[-1].copy()
    new_equal = equal.copy()
    old_equal = []
    plate.pop(-1)
    diag = np.diag(plate)
    res = float(epsilon + 1)  # Inicializar res com um valor maior que epsilon
    itera = 0

    while (res > epsilon and itera < maxiter):
        for i in range(len(equal)):
            old_equal = new_equal.copy()
            new_equal[i] = ((equal[i] + sum(plate[i])) / diag[i])

        res = np.max(np.abs(np.array(new_equal) - np.array(old_equal)))
        itera += 1

    print("Iterações:", itera)
    print("Aproximação:", res)
    return new_equal
