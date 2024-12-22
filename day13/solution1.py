import re

MAX_PRESS = 100
PRICE_A = 3
PRICE_B = 1

def parse_line(line):
    return tuple(map(int, re.findall(r'\b\d+\b', line)))

def vec_mult(pos_x, pos_y):
    return pos_x[0] * pos_y[1] - pos_x[1] * pos_y[0]

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return a // b
    return gcd(a // b, a % b)


def solve_eq(pos_a, pos_b, pos_prize):
    top_a = vec_mult(pos_b, pos_prize)
    bot_a = vec_mult(pos_b, pos_a)
    top_b = vec_mult(pos_a, pos_prize)
    bot_b = vec_mult(pos_a, pos_b)

    # this means that the buttons vectors are colinear.
    # if this is true, there might be more than one solution.
    if bot_a == 0:
        # this means that the buttons vectors aren't colinear
        # with the prize vector. therefore, there's no solution.
        if top_a != 0:
            return 0
        # otherwise, this is a system of linear Diophantine equations.
        # let's check if it has solutions in integers.
        gcd_x = gcd(pos_a[0], pos_b[0])
        gcd_y = gcd(pos_a[1], pos_b[1])
        if gcd_x % pos_prize[0] != 0 or gcd_y % pos_prize[1] != 0:
            return 0
        else:
            # now we need to find one of the solutions here,
            # but in reality the input doesn't contain those,
            # so let's skip :)
            raise "Can't solve!"
    # if the buttons vectors aren't colinear, the system of
    # equations has only one solution. let's check if it's
    # in integers.
    if top_a % bot_a != 0 or top_b % bot_b != 0:
        return 0
    # if it is, we need to check if the result is over
    # the maximim presses per button.
    res_a = top_a // bot_a
    res_b = top_b // bot_b
    if res_a > MAX_PRESS or res_b > MAX_PRESS:
        return 0
    # if all good, return the result price.
    else:
        return (top_a // bot_a) * PRICE_A + (top_b // bot_b) * PRICE_B

with open("input.txt") as f:
    lines = [line for line in f]
    res = 0
    for i in range(0, len(lines), 4):
        pos_a = parse_line(lines[i])
        pos_b = parse_line(lines[i + 1])
        pos_prize = parse_line(lines[i + 2])
        temp_res = solve_eq(pos_a, pos_b, pos_prize)
        res += temp_res
    print(res)
