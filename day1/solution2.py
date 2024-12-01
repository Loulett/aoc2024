with open("input.txt") as f:
    read_file = [int(x) for x in f.read().split()]
    count_dict_right = {}
    for r in read_file[1::2]:
        count_dict_right[r] = count_dict_right.get(r, 0) + 1
    print(sum(count_dict_right.get(l,0) * l for l in read_file[::2]))
