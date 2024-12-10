
def unzip_line(line):
    res = []
    cur_id = 0
    is_filled = True
    for s in line:
        num = int(s)
        if is_filled:
            res.extend([cur_id] * num)
            cur_id += 1
        else:
            res.extend([-1] * num)
        is_filled = not is_filled
    return res

def move_blocks(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] != -1:
            i += 1
        elif arr[j] == -1:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    return arr[:j]

def check_sum(arr):
    res = 0
    for i in range(0, len(arr)):
        res += i * arr[i]
    return res

with open("input.txt") as f:
    print(check_sum(move_blocks(unzip_line(f.readline()[:-1]))))
