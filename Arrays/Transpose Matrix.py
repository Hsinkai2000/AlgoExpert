def transposeMatrix(matrix):
    # Write your code here.
    final = []

    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        final.append(row)

    return final
