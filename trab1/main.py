def print_matrix(matrix, msg = ''):
    if msg !='':
        print(msg)
    for row in matrix:
        print(row)

def print_matrix_beautiful(matrix, msg = ''):
    if msg !='':
        print(msg)
    rows = len(matrix)
    cols = len(matrix[0])

    # Determinar a largura máxima para cada coluna
    column_widths = [max(len("{:.4f}".format(matrix[i][j])) if matrix[i][j] is not None else 0 for i in range(rows)) for j in range(cols)]

    # Imprimir a matrix com caracteres de moldura
    for i in range(rows):
        # Imprimir linha superior da célula
        line = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
        print(line)

        # Imprimir conteúdo da célula
        for j in range(cols):
            if matrix[i][j] is not None:
                cell = "| {:{width}.4f} ".format(matrix[i][j], width=column_widths[j])
            else:
                cell = "| {:{width}} ".format("", width=column_widths[j])
            print(cell, end="")
        print("|")

    # Imprimir linha inferior da célula
    line = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
    print(line)

def calculate_tx_points(plate):
    rows = len(plate)
    cols = len(plate[0])

    # Criar uma cópia da matrix 'plate' para armazenar os resultados
    # result = [[plate[i][j] for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if isinstance(plate[i][j], str) and plate[i][j].startswith('t'):
                sum_neighbors = 0
                count_neighbors = 0

                # Verificar os pontos vizinhos (acima, abaixo, esquerda e direita)
                if i > 0 and isinstance(plate[i - 1][j], int):
                    sum_neighbors += plate[i - 1][j]
                    count_neighbors += 1
                if i < rows - 1 and isinstance(plate[i + 1][j], int):
                    sum_neighbors += plate[i + 1][j]
                    count_neighbors += 1
                if j > 0 and isinstance(plate[i][j - 1], int):
                    sum_neighbors += plate[i][j - 1]
                    count_neighbors += 1
                if j < cols - 1 and isinstance(plate[i][j + 1], int):
                    sum_neighbors += plate[i][j + 1]
                    count_neighbors += 1

                if count_neighbors > 0:
                    plate[i][j] = sum_neighbors / count_neighbors
                else:
                    plate[i][j] = None

    return plate


# Exemplo de uso
plate = [
    [None, 25, 30, None, None],
    [70, 't1', 't2', 20, None],
    [80, 't3', 't4', 't5', 10],
    [100, 't6', 't7', 't8', 15],
    [None, 90, 110, 120, None]
]

tx_points = calculate_tx_points(plate)
tx_points = calculate_tx_points(tx_points)

print_matrix(tx_points, "Tx Points:")
print_matrix_beautiful(tx_points,"Tx Points:")
