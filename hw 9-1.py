import warnings
import numpy as np
from numpy.linalg import inv


filename = input("Enter a csv file: ")
try:
    data = np.genfromtxt(filename, delimiter=',')
    A = np.array(data[:, :-1])
    print("Matrix A")
    print(A)
    b = np.array(data[:, -1])
    print("Vector b")
    print(b)
    warnings.filterwarnings('ignore')
    try:
        det = np.linalg.det(A)
        print(f"Determinant of matrix is :{det:6.2f}")
        inv = np.linalg.inv(A)
        solution = np.linalg.solve(A, b)
        print()
        print("Solution for non-singular matrix:")
        print(f"Result= {solution}")
    except np.linalg.LinAlgError as e:
        try:
            Apinv = np.linalg.pinv(A)  # compute the pseudo inverse of Matrix A
            solution = Apinv.dot(b)
            print()
            print("Solution for singular matrix:")
            print(f"Result= {solution}")
        except np.linalg.LinAlgError as e:
            print("Invalid Matrix provided or few values are missing")
except FileNotFoundError:
    print("File not found")
except (OSError, IndexError) as e:
    print("File not found")
