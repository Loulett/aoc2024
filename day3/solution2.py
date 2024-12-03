import re
from math import prod

with open("input.txt") as f:
    memory = f.read()
    mult = re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', memory)
    res = 0
    enabled = True
    for m in mult:
        if m[1] != '':
            enabled = True
        elif m[2] != '':
            enabled = False
        elif enabled:
            res += prod(int(x) for x in re.findall(r'\d+', m[0]))
    print(res)
