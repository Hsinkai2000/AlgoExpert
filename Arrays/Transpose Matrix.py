def transposeMatrix(matrix):
    final = []  # Initialize the final transposed matrix

    # Iterate through columns of the original matrix
    for i in range(len(matrix[0])):
        row = []  # Initialize a new row for the transposed matrix
        # Iterate through rows of the original matrix
        for j in range(len(matrix)):
            row.append(matrix[j][i])  # Append the element to the new row
        final.append(row)  # Append the new row to the final matrix

    return final  # Return the transposed matrix
