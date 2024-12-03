import re
from math import prod

with open("input.txt") as f:
    memory = f.read()
    mult = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)
    res = 0
    for m in mult:
        res += prod(int(x) for x in re.findall(r'\d+', m))
    print(res)
