import sympy as sp


def format_vectors(vectors):
    if not vectors:
        return "empty"

    formatted = []
    for vec in vectors:
        elements = [sp.nsimplify(x) for x in vec]
        formatted.append(f"[{', '.join(map(str, elements))}]")
    return "\n".join(formatted)


def matrix_spaces(matrix):
    A = sp.Matrix(matrix)
    return {
        'column_space': A.columnspace(),
        'row_space': A.rowspace(),
        'null_space': A.nullspace(),
        'row_null_space': A.T.nullspace()
    }


def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1} (numbers separated by spaces): ").split()))
        if len(row) != cols:
            raise ValueError("Number of elements in the row does not match the number of columns!")
        matrix.append(row)
    return matrix


try:
    matrix = input_matrix()
    spaces = matrix_spaces(matrix)

    print("\nColumn Space Basis:")
    print(format_vectors(spaces['column_space']))

    print("\nRow Space Basis:")
    print(format_vectors(spaces['row_space']))

    print("\nNull Space Basis:")
    print(format_vectors(spaces['null_space']))

    print("\nRow Null Space Basis:")
    print(format_vectors(spaces['row_null_space']))

except Exception as e:
    print(f"Error: {str(e)}")
