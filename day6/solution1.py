
def find_guard_pos(matrix):
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            if matrix[y][x] == '^':
                return(y, x)

def in_map(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])

def move_guard(guard_pos, matrix, direction, visited):
    new_guard_pos = guard_pos
    while in_map(matrix, new_guard_pos) and not matrix[new_guard_pos[0]][new_guard_pos[1]] == '#':
        visited[new_guard_pos[0]][new_guard_pos[1]] = 1
        new_guard_pos = (new_guard_pos[0] + direction[0], new_guard_pos[1] + direction[1])
    if in_map(matrix, new_guard_pos):
        return (new_guard_pos[0] - direction[0], new_guard_pos[1] - direction[1])
    else:
        return new_guard_pos

with open("input.txt") as f:
    matrix = [line[:-1] for line in f]
    visited = [[0 for m in range(0, len(matrix[0]))] for m in range(0, len(matrix))]
    guard_y, guard_x = find_guard_pos(matrix)
    directions =[(-1, 0), (0, 1), (1, 0), (0, -1)]
    directions_pos = 0
    while in_map(matrix, (guard_y, guard_x)):
        guard_y, guard_x = move_guard((guard_y, guard_x), matrix, directions[directions_pos], visited)
        directions_pos = (directions_pos + 1) % 4
    print(sum(sum(visited[i]) for i in range(0, len(visited))))
