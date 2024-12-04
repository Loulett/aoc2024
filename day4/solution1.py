def coordinates_in_matrix(new_coordinates, matrix_size):
    return 0 <= new_coordinates[0] < matrix_size[0] and 0 <= new_coordinates[1] < matrix_size[1]

def move_coordinates(coor1, coor2):
    return (coor1[0]+coor2[0], coor1[1]+coor2[1])

def check_word(coordinates, direction, letters, matrix):
    if len(letters) == 0:
        return 1
    n, m = len(matrix), len(matrix[0])
    new_coordinates = move_coordinates(coordinates, direction)
    if coordinates_in_matrix(new_coordinates, (n, m)) and matrix[new_coordinates[0]][new_coordinates[1]] == letters[0]:
        return check_word(new_coordinates, direction, letters[1:], matrix)
    return 0

directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
letters = ['X', 'M', 'A', 'S']

with open("input.txt") as f:
    matrix = [line[:-1] for line in f]
    n, m = len(matrix), len(matrix[0])
    res = 0
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == letters[0]:
                for d in directions:
                    res += check_word((i, j), d, letters[1:], matrix)
    print(res)
