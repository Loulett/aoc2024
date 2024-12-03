def safe_diff(arr):
    for x in arr:
        if x == 0 or abs(x) > 3:
            return False
    return True

def monotone(arr):
    sign = arr[0] > 0
    for x in arr[1:]:
        if sign != (x > 0):
            return False
    return True

with open("input.txt") as f:
    safe_reports_count = 0
    for line in f:
        levels = [int(x) for x in line.split()]
        diff = [x - y for x, y in zip(levels[:len(levels)-1], levels[1:])]
        if safe_diff(diff) and monotone(diff):
            safe_reports_count += 1
    print(safe_reports_count)
