def transpose(A, rows, cols):
    AT = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            AT[j][i] = A[i][j]
    return AT


def multiply_matrix_vector(M, v, rows, cols):
    result = [0 for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i] += M[i][j] * v[j]
    return result


def dot_product(v1, v2, n):
    result = 0
    for i in range(n):
        result += v1[i] * v2[i]
    return result


def gaussian_elimination(A, rows, cols):
    M = [row[:] for row in A]
    pivot_row = 0
    pivot_col = 0

    while pivot_row < rows and pivot_col < cols:
        max_row = pivot_row
        for i in range(pivot_row + 1, rows):
            if abs(M[i][pivot_col]) > abs(M[max_row][pivot_col]):
                max_row = i
        M[pivot_row], M[max_row] = M[max_row], M[pivot_row]

        if abs(M[pivot_row][pivot_col]) < 1e-10:
            pivot_col += 1
            continue

        pivot = M[pivot_row][pivot_col]
        for j in range(cols):
            M[pivot_row][j] /= pivot
        for i in range(rows):
            if i != pivot_row:
                factor = M[i][pivot_col]
                for j in range(cols):
                    M[i][j] -= factor * M[pivot_row][j]
        pivot_row += 1
        pivot_col += 1

    return M


def find_nullspace(A, rows, cols):
    M = gaussian_elimination(A, rows, cols)
    rank = 0
    for i in range(rows):
        all_zero = True
        for j in range(cols):
            if abs(M[i][j]) > 1e-10:
                all_zero = False
                break
        if not all_zero:
            rank += 1

    free_vars = cols - rank
    if free_vars == 0:
        return [0] * cols

    basis = []
    pivot_cols = []
    for r in range(min(rows, cols)):
        for c in range(cols):
            if abs(M[r][c] - 1) < 1e-10:
                pivot_cols.append(c)
                break

    for free_col in range(cols):
        if free_col not in pivot_cols:
            vector = [0] * cols
            vector[free_col] = 1
            for r in range(len(pivot_cols)):
                pivot_col = pivot_cols[r]
                for c in range(cols):
                    if c == free_col:
                        vector[pivot_col] = -M[r][c]
            basis.append(vector)

    return basis[0] if basis else [0] * cols


print("Enter the number of rows in the matrix (rows):")
rows = int(input())
print("Enter the number of columns in the matrix (cols):")
cols = int(input())
A = []
print(f"Enter the matrix elements row by row ({rows} rows, each with {cols} numbers separated by spaces):")
for i in range(rows):
    print(f"Row {i + 1}:")
    row = list(map(float, input().split()))
    A.append(row)

AT = transpose(A, rows, cols)

y = find_nullspace(A, rows, cols)

x = find_nullspace(AT, cols, rows)

z = [0] * cols
for j in range(cols):
    if abs(A[0][j]) > 1e-10:
        z[j] = A[0][j]

print("x (vector orthogonal to the row space):", x)
print("A^T x =", multiply_matrix_vector(AT, x, cols, rows))
print("y (vector orthogonal to the column space):", y)
print("A y =", multiply_matrix_vector(A, y, rows, cols))
print("z (vector orthogonal to the nullspace):", z)
print("z dot y =", dot_product(z, y, cols))
