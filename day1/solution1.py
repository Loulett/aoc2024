with open("input.txt") as f:
    read_file = [int(x) for x in f.read().split()]
    print(sum(abs(x-y) for x, y in zip(sorted(read_file[::2]), sorted(read_file[1::2]))))
