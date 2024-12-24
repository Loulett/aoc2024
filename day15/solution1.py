def read_input(f):
    matrix = []
    line = f.readline()[:-1]
    while line != "":
        matrix.append(list(line))
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

def get_box_head(matrix, new_pos, direction):
    item = matrix[new_pos[0]][new_pos[1]]
    while item == 'O' or item == '@':
        new_pos = (new_pos[0]+direction[0], new_pos[1]+direction[1])
        item = matrix[new_pos[0]][new_pos[1]]
    return (new_pos[0]-direction[0], new_pos[1]-direction[1]), item

def move_robot(matrix, old_pos, direction):
    box_head_pos, next_item = get_box_head(matrix, old_pos, direction)
    if next_item == "#":
        return matrix, old_pos
    if next_item == '.':
        new_pos = old_pos[0] + direction[0], old_pos[1] + direction[1]
        matrix[old_pos[0]][old_pos[1]] = '.'
        matrix[new_pos[0]][new_pos[1]] = '@'
        if old_pos != box_head_pos:
            matrix[box_head_pos[0] + direction[0]][box_head_pos[1] + direction[1]] = 'O'
        return matrix, new_pos

def get_gps_coordinates(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O':
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
