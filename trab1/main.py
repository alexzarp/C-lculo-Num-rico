def calculate_tx_points(plate):
    rows = len(plate)
    cols = len(plate[0])

    # Criar uma cópia da matriz 'plate' para armazenar os resultados
    result = [[plate[i][j] for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if isinstance(plate[i][j], str) and plate[i][j].startswith('t'.lower()):
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
                    result[i][j] = sum_neighbors / count_neighbors
                else:
                    result[i][j] = None

    return result


# Exemplo de uso
plate = [
    [None, 25, 30, None, None],
    [70, 't1', 't2', 20, None],
    [80, 't3', 't4', 't5', 10],
    [100, 't6', 't7', 't8', 15],
    [None, 90, 110, 120, None]
]

tx_points = calculate_tx_points(plate)

print("Tx Points:")
for row in tx_points:
    print(row)
