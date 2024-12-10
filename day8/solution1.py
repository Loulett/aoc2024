def in_matrix(pos, matrix_size):
    return 0 <= pos[0] < matrix_size[0] and 0 <= pos[1] < matrix_size[1]

def maybe_add_antinode(pos, diff, matrix_size, antinodes):
    y, x = pos[0] + diff[0], pos[1] + diff[1]
    if in_matrix((y, x), matrix_size):
        antinodes.add((y, x))

def add_antinodes(antennas_pos, matrix_size, antinodes):
    for i in range(0, len(antennas_pos)):
        for j in range(i+1, len(antennas_pos)):
            y_i, x_i = antennas_pos[i]
            y_j, x_j = antennas_pos[j]
            y_diff, x_diff = y_i-y_j, x_i-x_j
            maybe_add_antinode((y_i, x_i), (y_diff, x_diff), matrix_size, antinodes)
            maybe_add_antinode((y_j, x_j), (-y_diff, -x_diff), matrix_size, antinodes)

with open("input.txt") as f:
    antennas = [line[:-1] for line in f]
    antennas_pos = dict()
    for y in range(0, len(antennas)):
        for x in range(0, len(antennas[0])):
            if antennas[y][x] != '.':
                pos = antennas_pos.get(antennas[y][x], set())
                pos.add((y,x))
                antennas_pos[antennas[y][x]] = pos
    antinodes = set()
    for key in antennas_pos:
        add_antinodes(list(antennas_pos[key]), (len(antennas), len(antennas[0])), antinodes)
    print(len(antinodes))
