import time
import random

def naive_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            result[i][j] = total

    return result


def split(M):
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def divide_conquer_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    C11 = add(divide_conquer_multiply(A11, B11), divide_conquer_multiply(A12, B21))
    C12 = add(divide_conquer_multiply(A11, B12), divide_conquer_multiply(A12, B22))
    C21 = add(divide_conquer_multiply(A21, B11), divide_conquer_multiply(A22, B21))
    C22 = add(divide_conquer_multiply(A21, B12), divide_conquer_multiply(A22, B22))

    result = []
    for i in range(n // 2):
        result.append(C11[i] + C12[i])
    for i in range(n // 2):
        result.append(C21[i] + C22[i])

    return result


def strassen_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    M1 = strassen_multiply(add(A11, A22), add(B11, B22))
    M2 = strassen_multiply(add(A21, A22), B11)
    M3 = strassen_multiply(A11, subtract(B12, B22))
    M4 = strassen_multiply(A22, subtract(B21, B11))
    M5 = strassen_multiply(add(A11, A12), B22)
    M6 = strassen_multiply(subtract(A21, A11), add(B11, B12))
    M7 = strassen_multiply(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    result = []
    for i in range(n // 2):
        result.append(C11[i] + C12[i])
    for i in range(n // 2):
        result.append(C21[i] + C22[i])

    return result


def get_matrix_from_user(name, size):
    print(f"Enter matrix {name} ({size}x{size}), row by row, space-separated:")
    matrix = []
    for i in range(size):
        row = input(f"Row {i+1}: ").split()
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix


def generate_random_matrix(size):
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]


def matrices_equal(A, B):
    return A == B


# ---- Main program ----

size = int(input("Enter matrix size (must be a power of 2, e.g. 2, 4, 8): "))
choice = input("Type 'r' for random matrices, or 'm' to enter manually: ")

if choice == 'r':
    A = generate_random_matrix(size)
    B = generate_random_matrix(size)
    print("Matrix A:", A)
    print("Matrix B:", B)
else:
    A = get_matrix_from_user("A", size)
    B = get_matrix_from_user("B", size)

start = time.time()
result_naive = naive_multiply(A, B)
time_naive = (time.time() - start) * 1000

start = time.time()
result_dc = divide_conquer_multiply(A, B)
time_dc = (time.time() - start) * 1000

start = time.time()
result_strassen = strassen_multiply(A, B)
time_strassen = (time.time() - start) * 1000

passed = matrices_equal(result_naive, result_dc) and matrices_equal(result_naive, result_strassen)

strassen_label = "Strassen's Algorithm"

print()
print(f"{'Method':<35}{'Time Taken'}")
print("-" * 50)
print(f"{'Naive Matrix Multiplication':<35}{time_naive:.2f} ms")
print(f"{'Divide and Conquer':<35}{time_dc:.2f} ms")
print(f"{strassen_label:<35}{time_strassen:.2f} ms")
print()
print("Verification Status:", "PASSED" if passed else "FAILED")      
