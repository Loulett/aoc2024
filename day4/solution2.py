def coordinates_in_matrix(new_coordinates, matrix_size):
    return 0 <= new_coordinates[0] < matrix_size[0] and 0 <= new_coordinates[1] < matrix_size[1]

def move_coordinates(coor1, coor2):
    return (coor1[0]+coor2[0], coor1[1]+coor2[1])

def check_word(coordinates, directions, letters, matrix):
    n, m = len(matrix), len(matrix[0])
    for d in directions:
        found_letters = set()
        for step in d:
            new_coordinates = move_coordinates(coordinates, step)
            if coordinates_in_matrix(new_coordinates, (n, m)):
                found_letters.add(matrix[new_coordinates[0]][new_coordinates[1]])
            else:
                return 0
        if letters != found_letters:
            return 0
    return 1

directions = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
letters = {'M', 'S'}

with open("input.txt") as f:
    matrix = [line[:-1] for line in f]
    n, m = len(matrix), len(matrix[0])
    res = 0
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 'A':
                res += check_word((i, j), directions, letters, matrix)
    print(res)
