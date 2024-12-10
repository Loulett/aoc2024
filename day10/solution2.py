
def in_matrix(pos, size):
    return 0 <= pos[0] < size[0] and 0 <= pos[1] < size[1]

def get_trail_score(position, matrix):
    i,j = position
    if matrix[i][j] == 9:
        return 1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = 0
    for d_i, d_j in directions:
        new_i, new_j = i + d_i, j + d_j
        if in_matrix((new_i, new_j), (len(matrix), len(matrix[0]))) and matrix[new_i][new_j] - matrix[i][j] == 1:
            res += get_trail_score((new_i, new_j), matrix)
    return res

with open("input.txt") as f:
    heights = [[int(x) for x in line[:-1]] for line in f]
    n, m = len(heights), len(heights[0])
    res = 0
    for i in range(0, n):
        for j in range(0, m):
            if heights[i][j] == 0:
                res += get_trail_score((i,j), heights)
    print(res)
