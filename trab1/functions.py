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