import sympy as sp

A = sp.Matrix([
    [1, 2, 1],
    [2, 4, 3],
    [3, 6, 4]
])

null_space = A.nullspace()
left_null_space = A.T.nullspace()
row_space = A.rowspace()

def get_fractions(vec):
    return [element.as_numer_denom() for element in vec]

x = get_fractions(null_space[0]) if null_space else []
y = get_fractions(left_null_space[0]) if left_null_space else []
z = get_fractions(row_space[0]) if row_space else []

print("Vector x (ortohogonal to row space):")
print([(int(num), int(den)) for num, den in x])

print("\nVector y (ortohogonal to row space):")
print([(int(num), int(den)) for num, den in y])

print("\nVector z (ortohogonal to row space):")
print([(int(num), int(den)) for num, den in z])
