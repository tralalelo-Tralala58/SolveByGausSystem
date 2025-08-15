def gauss_solve(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    m = cols - 1  # число переменных

    mat = [row[:] for row in matrix]
    rank = 0

    # Прямой ход
    for col in range(m):
        max_val = 1e-9
        pivot_row = -1
        for r in range(rank, rows):
            if abs(mat[r][col]) > max_val:
                max_val = abs(mat[r][col])
                pivot_row = r

        if pivot_row == -1:
            continue

        mat[rank], mat[pivot_row] = mat[pivot_row], mat[rank]

        for r in range(rank + 1, rows):
            factor = mat[r][col] / mat[rank][col]
            for c in range(col, cols):
                mat[r][c] -= factor * mat[rank][c]

        rank += 1
        if rank == rows:
            break

    # Проверим совместность
    for i in range(rank, rows):
        if abs(mat[i][m]) > 1e-9:  # правая часть != 0, а левая = 0
            return None

    if rank < m:
        return None

    x = [0.0] * m

    for i in range(m - 1, -1, -1):
        total = mat[i][m]  # правая часть
        for j in range(i + 1, m):
            total -= mat[i][j] * x[j]
        x[i] = total / mat[i][i]

    return x


def gauss(matrix):
    rows = len(matrix) # строки
    cols = len(matrix[0]) # столбцы
    mat = [row[:] for row in matrix] # копия
    rank = 0

    for col in range(cols):
        max_eval = 1e-9
        pivot_row = -1

        for row in range(rank, rows):
            if abs(mat[row][col]) > max_eval: # проходимся по столбцам
                max_eval = abs(mat[row][col])
                pivot_row = row

        if pivot_row == -1:
            continue  # столбец нулевой

        mat[rank], mat[pivot_row] = mat[pivot_row], mat[rank]

        # берем строки ниже ранга тк мы ее вывели наверх и далее обнуляем до ступенчатого вида
        for row in range(rank + 1, rows):
            factor = mat[row][col] / mat[rank][col]

            for c in range(col, cols):
                mat[row][c] -= factor * mat[rank][c]

        rank += 1
        if rank == rows:
            break

    return rank


def main():
    n, m = map(int, input().split())
    matrix = [[0] * (m + 1) for _ in range(n)]

    for i in range(n):
        x = [int(i) for i in input().split()]
        for j in range(m + 1):
            matrix[i][j] = x[j]

    A = [row[:-1] for row in matrix] # обычная матрица
    Ab = [row[:] for row in matrix] # расширенная матрица

    if gauss(Ab) != gauss(A):
        print('NO')
    elif gauss(A) < m:
        print('INF')
    else:
        solution = gauss_solve(matrix)
        if solution is None:
            print('NO')
        else:
            print('YES')
            print(' '.join(f"{val:.15f}" for val in solution))


if __name__ == '__main__':
    main()

# Sample Input:
#   кол-во строк
#   |
#   v
# 1)3 3 <-кол-во столбцов
# Sample Input:
# 
# 3 3
# 4 2 1 1
# 7 8 9 1
# 9 1 3 2