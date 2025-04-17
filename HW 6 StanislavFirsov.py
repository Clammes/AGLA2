import sympy as sp


def compute_eigen():
    while True:
        try:
            n = int(input("Enter square matrix size (N ≥ 3): "))
            if n < 3:
                print("Error: N must be ≥ 3")
                continue
            break
        except ValueError:
            print("Error: enter an integer")

    print(f"\nEnter {n}x{n} matrix row by row:")
    matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Row {i + 1} ({n} space-separated elements): ").split()
            if len(row_input) != n:
                print(f"Error: need {n} elements")
                continue
            try:
                row = [sp.sympify(x) for x in row_input]
                matrix.append(row)
                break
            except:
                print("Error: enter numbers or fractions (e.g., 2, -1/3, 5.5)")

    A = sp.Matrix(matrix)

    if A.shape[0] != A.shape[1]:
        print("Error: matrix must be square")
        return

    eigenvalues = A.eigenvals()
    eigenvectors = A.eigenvects()

    print("\nEigenvalues:")
    for eig, mult in eigenvalues.items():
        print(f"λ = {sp.pretty(eig)}")

    print("\nEigenvectors:")
    for vec in eigenvectors:
        eig, mult, basis = vec
        print(f"λ = {sp.pretty(eig)}")
        for idx, b in enumerate(basis, 1):
            vector = b.T.tolist()[0]
            formatted = [sp.nsimplify(x) for x in vector]
            print(f"Vector {idx}: {formatted}")
        print()


compute_eigen()
