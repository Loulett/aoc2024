import re
from math import prod

(lambda f: (lambda memory: print((lambda f: lambda arr, enabled, res: res if len(arr) == 0 else (f(f)(arr[1:], True, res) if arr[0][1] != '' else (f(f)(arr[1:], False, res) if arr[0][2] != '' else (f(f)(arr[1:], enabled, res + prod(int(x) for x in re.findall(r'\d+', arr[0][0]))) if enabled else f(f)(arr[1:], enabled, res)))))(lambda f: lambda arr, enabled, res: res if len(arr) == 0 else (f(f)(arr[1:], True, res) if arr[0][1] != '' else (f(f)(arr[1:], False, res) if arr[0][2] != '' else (f(f)(arr[1:], enabled, res + prod(int(x) for x in re.findall(r'\d+', arr[0][0]))) if enabled else f(f)(arr[1:], enabled, res)))))(re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', memory), True, 0)))([f.read(), f.close()][0]))(open("input.txt"))
