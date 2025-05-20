import numpy as np
import time

# Smaller matrices for faster execution
n, m = 100, 100
A = np.random.rand(n, m)
B = np.random.rand(n, m)

# Manual addition with loops
start = time.time()
C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
end = time.time()
print("Manual Addition Time:", end - start)

# Optimized addition using NumPy
start = time.time()
C_np = A + B
end = time.time()
print("NumPy Addition Time:", end - start)

# Manual multiplication with loops (naive)
start = time.time()
result = [
    [sum(A[i][k] * B[k][j] for k in range(m)) for j in range(m)] for i in range(n)
]
end = time.time()
print("Naive Multiplication Time:", end - start)

# NumPy multiplication
start = time.time()
result_np = np.dot(A, B)
end = time.time()
print("NumPy Multiplication Time:", end - start)

# Manual transpose
start = time.time()
transpose = [[A[j][i] for j in range(m)] for i in range(n)]
end = time.time()
print("Manual Transpose Time:", end - start)

# NumPy transpose
start = time.time()
transpose_np = np.transpose(A)
end = time.time()
print("NumPy Transpose Time:", end - start)
