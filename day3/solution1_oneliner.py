import re
from math import prod

(lambda f: (lambda data: print(sum(prod(int(x) for x in re.findall(r'\d+', m)) for m in re.findall(r'mul\(\d{1,3},\d{1,3}\)', data))))([f.read(), f.close()][0]))(open("input.txt"))
