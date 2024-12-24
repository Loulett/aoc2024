def read_input(f):
    matrix = []
    line = f.readline()[:-1]
    while line != "":
        zipped_line = list(line)
        unzipped_line = []
        for s in zipped_line:
            if s == '#':
                unzipped_line.extend(['#', '#'])
            if s == 'O':
                unzipped_line.extend(['[', ']'])
            if s == '.':
                unzipped_line.extend(['.', '.'])
            if s == '@':
                unzipped_line.extend(['@', '.'])
        matrix.append(unzipped_line)
        line = f.readline()[:-1]
    directions = []
    line = f.readline()[:-1]
    while line != "":
        directions.extend(list(line))
        line = f.readline()[:-1]
    return matrix, directions

def get_robot_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '@':
                return (i, j)

def get_move_matrix(move_matrix, pos, matrix, direction):
    if matrix[pos[0]][pos[1]] == '#':
        return move_matrix, False
    if matrix[pos[0]][pos[1]] == '.':
        return move_matrix, True
    if matrix[pos[0]][pos[1]] in "[]":
        new_pos1 = (pos[0] + direction[0], pos[1] + direction[1])
        move_matrix[new_pos1[0]][new_pos1[1]] = 1
        # if the movement is to the left or to the right, we can't move more than one row of boxes
        if direction in [(0, 1), (0, -1)]:
            return get_move_matrix(move_matrix, new_pos1, matrix, direction)
        else:
            if matrix[pos[0]][pos[1]] == '[':
                move_matrix[pos[0] + direction[0]][pos[1] + direction[1] + 1] = 1
            if matrix[pos[0]][pos[1]] == ']':
                move_matrix[pos[0] + direction[0]][pos[1] + direction[1] - 1] = 1
            move_matrix1, res1 = get_move_matrix(move_matrix, new_pos1, matrix, direction)
            move_matrix2, res2 = get_move_matrix(move_matrix, (new_pos1[0], new_pos1[1] + 1 if matrix[pos[0]][pos[1]] == '[' else new_pos1[1] - 1), matrix, direction)
            # as we're not doing a deep copy in the recursion, move_matrix1 and move_matrix2 are the same.
            return move_matrix1, res1 and res2

def redraw_matrix(matrix, move_matrix, direction):
    s = "[]"
    for i in range(len(matrix)):
        bit = 0
        for j in range(len(matrix[0])):
            if move_matrix[i][j] == 1:
                matrix[i][j] = s[bit]
                if move_matrix[i - direction[0]][j - direction[1]] != 1:
                    matrix[i - direction[0]][j - direction[1]] = '.'
                bit = (bit + 1) % 2
    return matrix

def move_robot(matrix, old_pos, direction):
    move_matrix = [[0] * len(matrix[0]) for i in range(len(matrix))]
    new_pos = old_pos[0] + direction[0], old_pos[1] + direction[1]
    move_matrix, can_move = get_move_matrix(move_matrix, new_pos, matrix, direction)
    if not can_move:
        return matrix, old_pos
    else:
        matrix = redraw_matrix(matrix, move_matrix, direction)
        matrix[old_pos[0]][old_pos[1]] = '.'
        matrix[new_pos[0]][new_pos[1]] = '@'
        return matrix, new_pos

def get_gps_coordinates(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '[':
                res += (100 * i + j)
    return res

def pretty_print(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()

with open("input.txt") as f:
    dir_map = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    matrix, directions = read_input(f)
    robot_pos = get_robot_pos(matrix)
    for d in directions:
        matrix, robot_pos = move_robot(matrix, robot_pos, dir_map[d])
    pretty_print(matrix)
    print(get_gps_coordinates(matrix))
