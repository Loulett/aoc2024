from queue import Queue

def in_matrix(pos, size):
    return 0 <= pos[0] < size[0] and 0 <= pos[1] < size[1]

def get_region(pos, regions, visited):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    letter = regions[pos[0]][pos[1]]
    q = Queue()
    q.put(pos)
    res_area = 0
    res_perimiter = 0
    while not q.empty():
        x, y = q.get()
        if visited[x][y]:
            continue
        visited[x][y] = True
        res_area += 1
        temp_perimiter = 4
        for d in directions:
            new_x, new_y = x + d[0], y + d[1]
            if in_matrix((new_x, new_y), (len(regions), len(regions[0]))) and regions[new_x][new_y] == letter:
                temp_perimiter -= 1
                if not visited[new_x][new_y]:
                    q.put((new_x, new_y))
        res_perimiter += temp_perimiter
    return res_perimiter, res_area


with open("input.txt") as f:
    regions = [line[:-1] for line in f]
    visited = [[False] * len(regions[0]) for i in range(len(regions))]
    res = 0
    for i in range(len(regions)):
        for j in range(len(regions[0])):
            if not visited[i][j]:
                perimiter, area = get_region((i, j), regions, visited)
                res += (perimiter * area)
    print(res)
