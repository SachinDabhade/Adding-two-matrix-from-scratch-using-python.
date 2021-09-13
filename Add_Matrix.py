# Practice problem 15
# This is the practice problem on how to add two matrix in python

def Take_Matrix(row, column):
    matrix = []
    for i in range(row):
        print(f"This is row {i + 1}...!")
        raw_row = []
        for j in range(column):
            number = int(input(f"Enter the number {j + 1}: "))
            raw_row.append(number)
        matrix.append(raw_row)
    return matrix

def Add_Matrix(A, B):
    Matrix = []
    for i in range(row):
        Row = []
        for j in range(column):
            number = A[i][j] + B[i][j]
            Row.append(number)
        Matrix.append(Row)
    return Matrix

if __name__ == '__main__':
    while True:
        choice = 0
        try:
            row = int(input("How many rows do you want in your matrix: "))
            column = int(input("How many column do you want in your matrix: "))
        except Exception as e:
            print('Only integers are allowed...!')
        else:
            print("\nMatrix A: \n")
            A = Take_Matrix(row, column)
            print(f"This is the A matrix: {A}")

            print("\nMatrix B: \n")
            B = Take_Matrix(row, column)
            print(f"This is the B matrix: {B}")

            print("\nAdding the Matrices...!\n")
            print(f"Addition of the matrices is {Add_Matrix(A, B)}")
            print("\nThis is done...!\n")
        continue
