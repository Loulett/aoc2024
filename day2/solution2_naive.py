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

def check_if_diff_is_valid(arr):
    diff = [x - y for x, y in zip(arr[:len(arr)-1], arr[1:])]
    return safe_diff(diff) and monotone(diff)

with open("input.txt") as f:
    safe_reports_count = 0
    for line in f:
        levels = [int(x) for x in line.split()]
        for i in range(0, len(levels)):
            if check_if_diff_is_valid(levels[:i] + levels[(i+1):]):
                print(levels)
                safe_reports_count += 1
                break
    print(safe_reports_count)
