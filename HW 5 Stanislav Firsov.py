import numpy as np

def gram_schmidt(vectors):
    orthogonal_vectors = []

    for v in vectors:
        v_orth = v.copy()
        for u in orthogonal_vectors:
            v_orth -= np.dot(v, u) / np.dot(u, u) * u
        orthogonal_vectors.append(v_orth)

    return np.array(orthogonal_vectors)


n = int(input("Enter the number of vectors: "))
m = int(input("Enter the dimension of each vector: "))

vectors = []
print("Enter each vector as space-separated values:")
for _ in range(n):
    vector = list(map(float, input().split()))
    if len(vector) != m:
        print("Error: Incorrect vector dimension.")
        exit()
    vectors.append(vector)

vectors = np.array(vectors, dtype=float)
orthogonalized_vectors = gram_schmidt(vectors)

print("Orthogonalized vectors:")
print(orthogonalized_vectors)
