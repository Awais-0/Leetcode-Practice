def matrix_transpose(matrix):
    output = [[],[],[]]
    for j in range(len(matrix)):
        row = matrix[j]
        out_row = output[j]
        for i in range(len(row)):
            out_row[i] = row[i]
    return output

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix_transpose(matrix=matrix))