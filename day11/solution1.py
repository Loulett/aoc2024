
def notation(num):
    res = 0
    while num != 0:
        num = num // 10
        res += 1
    return res

def split_stone(num, notation):
    divider = 10 ** (notation // 2)
    return [num // divider, num % divider]


def update_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        n = notation(stone)
        if n % 2 == 1:
            new_stones.append(stone * 2024)
        else:
            new_stones.extend(split_stone(stone, n))
    return new_stones


with open("input.txt") as f:
    stones = [int(x) for x in f.readline().split()]
    print(stones)
    for i in range(25):
        stones = update_stones(stones)
        print(stones)
    print(len(stones))
