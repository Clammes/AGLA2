import numpy as np


def gauss_jordan_inverse(matrix):
    n = len(matrix)
    aug_matrix = np.hstack((matrix, np.identity(n)))

    for i in range(n):
        if aug_matrix[i, i] == 0:
            for j in range(i + 1, n):
                if aug_matrix[j, i] != 0:
                    aug_matrix[[i, j]] = aug_matrix[[j, i]]
                    break
            else:
                raise ValueError("Matrix is singular and cannot be inverted.")

        aug_matrix[i] /= aug_matrix[i, i]

        for j in range(n):
            if i != j:
                aug_matrix[j] -= aug_matrix[j, i] * aug_matrix[i]

    return aug_matrix[:, n:]


if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    if rows != columns:
        print("You can't invert not square matrix :(")
    print("Enter the elements of the matrix row by row, separating numbers with spaces:")
    A = np.array([list(map(float, input().split())) for _ in range(rows)])

    try:
        inverse_A = gauss_jordan_inverse(A)
        print("Inverse matrix:")
        print(inverse_A)
    except ValueError as e:
        print(e)
