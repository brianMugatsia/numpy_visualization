import numpy as np

def add_matrices(A, B):
    return A + B


def subtract_matrices(A, B):
    return A - B


def multiply_matrices(A, B):
    return np.dot(A, B)


def matrix_determinant(A):
    return np.linalg.det(A)


def matrix_inverse(A):
    return np.linalg.inv(A)


def solve_linear_equations(A, B):
    """
    Solves AX = B
    """
    return np.linalg.solve(A, B)


def main():
    print(" NumPy Matrix Calculator")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Determinant")
    print("5. Inverse")
    print("6. Solve linear equations (AX = B)")

    choice = int(input("Choose an option (1-6): "))

    if choice in [1, 2, 3]:
        A = np.array(eval(input("Enter Matrix A (e.g. [[1,2],[3,4]]): ")))
        B = np.array(eval(input("Enter Matrix B: ")))

        if choice == 1:
            result = add_matrices(A, B)
        elif choice == 2:
            result = subtract_matrices(A, B)
        else:
            result = multiply_matrices(A, B)

        print("Result:\n", result)

    elif choice == 4:
        A = np.array(eval(input("Enter square matrix: ")))
        print("Determinant:", matrix_determinant(A))

    elif choice == 5:
        A = np.array(eval(input("Enter square matrix: ")))
        print("Inverse:\n", matrix_inverse(A))

    elif choice == 6:
        A = np.array(eval(input("Enter coefficient matrix A: ")))
        B = np.array(eval(input("Enter constants matrix B: ")))
        print("Solution X:\n", solve_linear_equations(A, B))

    else:
        print(" Invalid choice")


if __name__ == "__main__":
    main()
