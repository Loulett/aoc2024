
def parse_input(line):
    return [tuple(int(x) for x in match[2:].split(",")) for match in line.split()]

def count_new_pos(old_pos, vel, size):
    return ((old_pos[0] + vel[0]) % size[0], (old_pos[1] + vel[1]) % size[1])

def update_positions(positions, size):
    new_positions = []
    for pos, vel in positions:
        new_positions.append((count_new_pos(pos, vel, size), vel))
    return new_positions

def has_long_line(robot_map):
    long_line = "##############"
    for i in range(len(robot_map)):
        if long_line in ''.join(robot_map[i]):
            return True
    return False

def pretty_print_if_has_line(positions, size, step):
    robot_map = [["."] * size[1] for i in range(size[0])]
    for pos, vel in positions:
        robot_map[pos[0]][pos[1]] = "#"

    if has_long_line(robot_map):
        print(step)
        for i in range(size[0]):
            print(''.join(robot_map[i]))
        print()

with open("input.txt") as f:
    n, m = 101, 103
    old_map = [[0] * m for i in range(n)]
    positions = []
    for line in f:
        pos, vel = parse_input(line)
        positions.append((pos, vel))
    for i in range(10000):
        pretty_print_if_has_line(positions, (n, m), i)
        positions = update_positions(positions, (n, m))
