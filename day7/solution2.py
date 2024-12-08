
def parse_line(line):
    val = line.split()
    return int(val[0][:-1]), [int(x) for x in val[1:]]

def comb(x, y):
    return int(str(x) + str(y))

def can_create_equation(result, values, temp_res):
    if temp_res > result:
        return False
    if len(values) == 0:
        return result == temp_res
    return can_create_equation(result, values[1:], temp_res + values[0]) or can_create_equation(result, values[1:], temp_res * values[0]) or can_create_equation(result, values[1:], comb(temp_res, values[0]))

with open("input.txt") as f:
    res = 0
    for line in f:
        result, values = parse_line(line)
        res += result if can_create_equation(result, values[1:], values[0]) else 0
    print(res)
