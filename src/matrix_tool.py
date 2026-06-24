import numpy as np


def input_matrix(matrix_name):
    rows = int(input(f"\nEnter number of rows for Matrix {matrix_name}: "))
    cols = int(input(f"Enter number of columns for Matrix {matrix_name}: "))

    print(f"\nEnter elements row-wise for Matrix {matrix_name}:")

    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))

        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))

        matrix.append(row)

    return np.array(matrix)


def display_matrix(matrix, title="Result"):
    print(f"\n{title}")
    print("-" * 30)
    print(matrix)
    print("-" * 30)


def main():
    while True:
        print("\n===== MATRIX OPERATIONS TOOL =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("\nChoose an operation (1-6): ")

        try:
            if choice in ['1', '2', '3']:
                A = input_matrix("A")
                B = input_matrix("B")

                if choice == '1':
                    if A.shape != B.shape:
                        print("\nError: Matrices must have the same dimensions.")
                    else:
                        display_matrix(A + B, "Addition Result")

                elif choice == '2':
                    if A.shape != B.shape:
                        print("\nError: Matrices must have the same dimensions.")
                    else:
                        display_matrix(A - B, "Subtraction Result")

                elif choice == '3':
                    if A.shape[1] != B.shape[0]:
                        print("\nError: Columns of Matrix A must equal rows of Matrix B.")
                    else:
                        display_matrix(np.matmul(A, B), "Multiplication Result")

            elif choice == '4':
                A = input_matrix("A")
                display_matrix(A.T, "Transpose Result")

            elif choice == '5':
                A = input_matrix("A")

                if A.shape[0] != A.shape[1]:
                    print("\nError: Determinant can only be calculated for square matrices.")
                else:
                    det = np.linalg.det(A)
                    print(f"\nDeterminant = {round(det, 2)}")

            elif choice == '6':
                print("\nThank you for using Matrix Operations Tool!")
                break

            else:
                print("\nInvalid choice.")

        except ValueError:
            print("\nPlease enter valid numeric values.")

        except Exception as e:
            print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()