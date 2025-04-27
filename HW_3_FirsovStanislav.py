def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:.2f}" for x in row])
    print()

def matrix_transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

def gaussian_elimination(matrix):
    m, n = len(matrix), len(matrix[0])
    A = [row[:] for row in matrix]
    pivot_positions = []
    row, col = 0, 0

    while row < m and col < n:
        pivot_row = row
        while pivot_row < m and abs(A[pivot_row][col]) < 1e-10:
            pivot_row += 1
        if pivot_row == m:
            col += 1
            continue

        if pivot_row != row:
            A[row], A[pivot_row] = A[pivot_row], A[row]

        pivot = A[row][col]
        for j in range(n):
            A[row][j] /= pivot

        for i in range(m):
            if i != row:
                factor = A[i][col]
                for j in range(n):
                    A[i][j] -= factor * A[row][j]

        pivot_positions.append(col)
        row += 1
        col += 1

    return A, pivot_positions

def column_space(matrix, pivot_cols):
    return [[matrix[i][j] for i in range(len(matrix))] for j in pivot_cols]

def row_space(rref, pivot_cols):
    return [rref[i][:] for i in range(len(rref)) if any(abs(x) > 1e-10 for x in rref[i])]

def null_space(matrix, pivot_cols):
    m, n = len(matrix), len(matrix[0])
    rref, _ = gaussian_elimination(matrix)
    free_vars = [j for j in range(n) if j not in pivot_cols]
    if not free_vars:
        return [[0] * n]

    basis = []
    for free_var in free_vars:
        x = [0] * n
        x[free_var] = 1
        for pivot_col, row in zip(pivot_cols, range(len(pivot_cols))):
            x[pivot_col] = -rref[row][free_var]
        basis.append(x)
    return basis

def compute_matrix_spaces(matrix):
    rref, pivot_cols = gaussian_elimination(matrix)
    
    col_space = column_space(matrix, pivot_cols)
    
    row_sp = row_space(rref, pivot_cols)
    
    col_null_sp = null_space(matrix, pivot_cols)
    
    matrix_T = matrix_transpose(matrix)
    _, pivot_cols_T = gaussian_elimination(matrix_T)
    row_null_sp = null_space(matrix_T, pivot_cols_T)
    
    return col_space, row_sp, col_null_sp, row_null_sp

def read_matrix_from_console():
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            if rows <= 0:
                print("Number of rows must be positive.")
                continue
            cols = int(input("Enter the number of columns: "))
            if cols <= 0:
                print("Number of columns must be positive.")
                continue
            break
        except ValueError:
            print("Please enter valid integers for rows and columns.")

    print(f"Enter the matrix elements row by row ({rows} rows, {cols} columns):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter {cols} elements for row {i+1} (space-separated): ")
                row = [float(x) for x in row_input.split()]
                if len(row) != cols:
                    print(f"Expected {cols} elements, got {len(row)}. Try again.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Please enter valid numbers.")
    
    return matrix

def main():
    matrix = read_matrix_from_console()
    
    print("\nOriginal Matrix:")
    print_matrix(matrix, "A")
    
    col_space, row_space, col_null_space, row_null_space = compute_matrix_spaces(matrix)
    
    print("Column Space Basis:")
    print_matrix(col_space, "C")
    
    print("Row Space Basis:")
    print_matrix(row_space, "R")
    
    print("Column Null Space Basis:")
    print_matrix(col_null_space, "N")
    
    print("Row Null Space Basis:")
    print_matrix(row_null_space, "LN")

if __name__ == "__main__":
    main()
