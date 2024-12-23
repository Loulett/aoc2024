
def parse_input(line):
    return [tuple(int(x) for x in match[2:].split(",")) for match in line.split()]

def count_new_pos(old_pos, vel, size):
    return ((old_pos[0] + vel[0] * 100) % size[0], (old_pos[1] + vel[1] * 100) % size[1])

with open("input.txt") as f:
    n, m = 101, 103
    q = [[0,0],[0,0]]
    for line in f:
        pos, vel = parse_input(line)
        pos = count_new_pos(pos, vel, (n, m))
        if pos[0] != n // 2 and pos[1] != m // 2:
            q[pos[0] > n // 2][pos[1] > m // 2] += 1
    print(q[0][0]*q[0][1]*q[1][0]*q[1][1])
