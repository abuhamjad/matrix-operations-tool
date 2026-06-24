import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np


class MatrixTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Operations Tool")
        self.root.geometry("800x700")
        self.root.resizable(False, False)
        self.current_result = ""

        title = tk.Label(
            root,
            text="Matrix Operations Tool",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # Matrix A
        tk.Label(root, text="Matrix A", font=("Arial", 14, "bold")).pack()

        self.matrix_a = tk.Text(root, height=6, width=40)
        self.matrix_a.pack(pady=5)

        tk.Label(
            root,
            text="Enter rows separated by new lines and elements separated by spaces",
            fg="gray"
        ).pack()

        # Matrix B
        tk.Label(root, text="Matrix B", font=("Arial", 14, "bold")).pack(pady=(20, 0))

        self.matrix_b = tk.Text(root, height=6, width=40)
        self.matrix_b.pack(pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame,
            text="Add",
            width=15,
            command=self.add_matrices
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Subtract",
            width=15,
            command=self.subtract_matrices
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Multiply",
            width=15,
            command=self.multiply_matrices
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Transpose A",
            width=15,
            command=self.transpose_matrix
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Determinant A",
            width=15,
            command=self.determinant_matrix
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Inverse A",
            width=15,
            command=self.inverse_matrix
        ).grid(row=1, column=2, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Rank A",
            width=15,
            command=self.rank_matrix
        ).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Save Result",
            width=15,
            command=self.save_result
        ).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Clear",
            width=15,
            command=self.clear_all
        ).grid(row=2, column=2, padx=5, pady=5)

        # Result Area
        tk.Label(root, text="Result", font=("Arial", 14, "bold")).pack()

        self.result_box = tk.Text(
            root,
            height=10,
            width=60,
            state="disabled",
            bg="#f4f4f4"
        )
        self.result_box.pack(pady=10)

    def get_matrix(self, text_widget):
        try:
            data = text_widget.get("1.0", tk.END).strip().split("\n")

            matrix = []
            for row in data:
                matrix.append(list(map(float, row.split())))

            return np.array(matrix)

        except ValueError:
            raise ValueError("Please enter valid numeric values.")

    def display_result(self, result):
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.END, self.current_result)
        self.result_box.config(state="disabled")

    def add_matrices(self):
        try:
            A = self.get_matrix(self.matrix_a)
            B = self.get_matrix(self.matrix_b)

            if A.shape != B.shape:
                raise ValueError("Matrices must have the same dimensions.")

            self.display_result(A + B)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def subtract_matrices(self):
        try:
            A = self.get_matrix(self.matrix_a)
            B = self.get_matrix(self.matrix_b)

            if A.shape != B.shape:
                raise ValueError("Matrices must have the same dimensions.")

            self.display_result(A - B)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def multiply_matrices(self):
        try:
            A = self.get_matrix(self.matrix_a)
            B = self.get_matrix(self.matrix_b)

            if A.shape[1] != B.shape[0]:
                raise ValueError(
                    "Columns of Matrix A must equal rows of Matrix B."
                )

            self.display_result(np.matmul(A, B))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def transpose_matrix(self):
        try:
            A = self.get_matrix(self.matrix_a)
            self.display_result(A.T)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def determinant_matrix(self):
        try:
            A = self.get_matrix(self.matrix_a)

            if A.shape[0] != A.shape[1]:
                raise ValueError(
                    "Determinant can only be calculated for square matrices."
                )

            det = np.linalg.det(A)
            self.display_result(f"Determinant = {round(det, 2)}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def inverse_matrix(self):
        try:
            A = self.get_matrix(self.matrix_a)

            # Check if matrix is square
            if A.shape[0] != A.shape[1]:
                raise ValueError(
                    "Inverse can only be calculated for square matrices."
                )

            # Check if determinant is zero
            if np.linalg.det(A) == 0:
                raise ValueError(
                    "Matrix is singular and has no inverse."
                )

            inverse = np.linalg.inv(A)

            self.display_result(np.round(inverse, 2))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def rank_matrix(self):
        try:
            A = self.get_matrix(self.matrix_a)

            rank = np.linalg.matrix_rank(A)

            self.display_result(f"Rank of Matrix A = {rank}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_result(self):
        if not self.current_result:
            messagebox.showwarning(
                "No Result",
                "Please perform an operation first."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write("Matrix Operations Tool Result\n")
                    file.write("=" * 35 + "\n\n")
                    file.write(self.current_result)

                messagebox.showinfo(
                    "Success",
                    "Result saved successfully!"
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))

    def clear_all(self):
        self.matrix_a.delete("1.0", tk.END)
        self.matrix_b.delete("1.0", tk.END)

        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)
        self.result_box.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixTool(root)
    root.mainloop()