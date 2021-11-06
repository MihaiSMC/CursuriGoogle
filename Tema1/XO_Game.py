def print_table(matrix):
    for row in matrix:
        for el in row:
            if el == 1:
                print('X|', end="")
            elif el == 0:
                print('O|', end="")
            else:
                print(' |', end="")
        print()


def print_matrix(matrix):
    for row in matrix:
        print('|'.join(map(str, row)))


def verify_table(matrix):
    for i in range(0, 3):
        if matrix[i] == [1] * 3:
            return 1
        if matrix[i] == [0] * 3:
            return 0

    for i in range(0, 3):
        column = [row[i] for row in matrix]
        if column == [1] * 3:
            return 1
        if column == [0] * 3:
            return 0

    prim_diag = [row[i] for i, row in enumerate(matrix)]
    sec_diag = [row[2 - i] for i, row in enumerate(matrix)]

    if prim_diag == [1] * 3 or sec_diag == [1] * 3:
        return 1
    if prim_diag == [0] * 3 or sec_diag == [0] * 3:
        return 0

    sem = 0
    for x in matrix:
        if -1 in x:
            sem = 1

    if sem == 0:
        return 2

    return -1


def main():
    matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

    while True:
        index = int(input("Alege un index (1-9): "))
        if matrix[(index - 1)//3][index % 3 - 1] != -1:
            print("Index-ul selectat este ocupat\n")
            continue

        matrix[(index - 1)//3][index % 3 - 1] = 1
        print_table(matrix)
        print()

        if verify_table(matrix) == 1:
            print("YOU WON")
            break
        elif verify_table(matrix) == 0:
            print("YOU LOST")
            break
        elif verify_table(matrix) == 2:
            print("DRAW")
            break

        if matrix[1][1] == -1:
            matrix[1][1] = 0
        elif matrix[0][0] == -1:
            matrix[0][0] = 0
        elif matrix[0][2] == -1:
            matrix[0][2] = 0
        elif matrix[2][0] == -1:
            matrix[2][0] = 0
        elif matrix[2][2] == -1:
            matrix[2][2] = 0
        elif matrix[0][1] == -1:
            matrix[0][1] = 0
        elif matrix[1][0] == -1:
            matrix[1][0] = 0
        elif matrix[1][2] == -1:
            matrix[1][2] = 0
        elif matrix[2][1] == -1:
            matrix[2][1] = 0

        print("Adversarul a ales: ")
        print_table(matrix)
        print()

        if verify_table(matrix) == 1:
            print("YOU WON")
            break
        elif verify_table(matrix) == 0:
            print("YOU LOST")
            break
        elif verify_table(matrix) == 2:
            print("DRAW")
            break


if __name__ == "__main__":
    main()
