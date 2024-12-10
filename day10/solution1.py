
def get_empty_matrix(size):
    return [[False] * size[1] for i in range(size[0])]

def in_matrix(pos, size):
    return 0 <= pos[0] < size[0] and 0 <= pos[1] < size[1]

def get_trail_score(position, matrix, visited):
    i,j = position
    if matrix[i][j] == 9:
        res = 0 if visited[i][j] else 1
        visited[i][j] = True
        return res
    visited[i][j] = True
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = 0
    for d_i, d_j in directions:
        new_i, new_j = i + d_i, j + d_j
        if in_matrix((new_i, new_j), (len(matrix), len(matrix[0]))) and matrix[new_i][new_j] - matrix[i][j] == 1:
            res += get_trail_score((new_i, new_j), matrix, visited)
    return res

with open("input.txt") as f:
    heights = [[int(x) for x in line[:-1]] for line in f]
    n, m = len(heights), len(heights[0])
    res = 0
    for i in range(0, n):
        for j in range(0, m):
            if heights[i][j] == 0:
                res += get_trail_score((i,j), heights, get_empty_matrix((n, m)))
    print(res)
