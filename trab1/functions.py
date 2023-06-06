def print_matrix(matrix, msg = ''):
    if msg !='':
        print(msg)
    for row in matrix:
        print(row)

def int_to_float(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if isinstance(mat[i][j], int):
                mat[i][j] = float(mat[i][j])
    return mat

def print_matrix_beautiful(matrix, msg = ''):
    if msg !='':
        print(msg)
    rows = len(matrix)
    cols = len(matrix[0])

    column_widths = [max(len("{:.4f}".format(matrix[i][j])) if matrix[i][j] is not None else 0 for i in range(rows)) for j in range(cols)]

    for i in range(rows):
        line = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
        print(line)

        for j in range(cols):
            if matrix[i][j] is not None:
                cell = "| {:{width}.4f} ".format(matrix[i][j], width=column_widths[j])
            else:
                cell = "| {:{width}} ".format("", width=column_widths[j])
            print(cell, end="")
        print("|")

    line = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
    print(line)

def calculate_tx_points(plate):
    rows = len(plate)
    cols = len(plate[0])

    int_to_float(plate)

    for i in range(rows):
        for j in range(cols):
            if isinstance(plate[i][j], str) and plate[i][j].startswith('t'):
                sum_neighbors = 0
                count_neighbors = 0

                if i > 0 and isinstance(plate[i - 1][j], float):
                    sum_neighbors += plate[i - 1][j]
                    count_neighbors += 1
                if i < rows - 1 and isinstance(plate[i + 1][j], float):
                    sum_neighbors += plate[i + 1][j]
                    count_neighbors += 1
                if j > 0 and isinstance(plate[i][j - 1], float):
                    sum_neighbors += plate[i][j - 1]
                    count_neighbors += 1
                if j < cols - 1 and isinstance(plate[i][j + 1], float):
                    sum_neighbors += plate[i][j + 1]
                    count_neighbors += 1

                if count_neighbors > 0:
                    plate[i][j] = sum_neighbors / count_neighbors
                else:
                    plate[i][j] = None

    return plate

def gauss_seidel(matrix, epsilon = 1e-6):
    rows = len(matrix)
    cols = len(matrix[0])

    # Criar uma matriz auxiliar para armazenar os resultados das iterações
    result_matrix = [[0.0 for _ in range(cols)] for _ in range(rows)]

    # Definir o critério de convergência (número máximo de iterações)
    max_iterations = 100

    # Executar as iterações do método Gauss-Seidel
    for _ in range(max_iterations):
        max_diff = 0.0  # Para verificar a convergência

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] is not None:
                    old_value = result_matrix[i][j]

                    # Calcular a média dos pontos vizinhos
                    total = 0.0
                    count = 0

                    if i > 0 and matrix[i-1][j] is not None:
                        total += result_matrix[i-1][j]
                        count += 1
                    if i < rows-1 and matrix[i+1][j] is not None:
                        total += result_matrix[i+1][j]
                        count += 1
                    if j > 0 and matrix[i][j-1] is not None:
                        total += result_matrix[i][j-1]
                        count += 1
                    if j < cols-1 and matrix[i][j+1] is not None:
                        total += result_matrix[i][j+1]
                        count += 1

                    if count > 0:
                        result_matrix[i][j] = total / count

                    # Verificar a diferença entre o valor atual e o anterior
                    diff = abs(result_matrix[i][j] - old_value)
                    if diff > max_diff:
                        max_diff = diff

        # Verificar a convergência
        if max_diff < epsilon:
            break

    return result_matrix
