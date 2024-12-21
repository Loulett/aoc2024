
def read_input(file):
    rules = dict()
    seqs = []
    for line in file:
        if "|" in line:
            x, y = (int(i) for i in line.split("|"))
            rule = rules.get(x, set())
            rule.add(y)
            rules[x] = rule
        elif "," in line:
            seqs.append([int(x) for x in line.split(",")])
        else:
            continue
    return rules, seqs

def is_valid(pages, rules):
    for i in range(len(pages)):
        for j in range(i+1, len(pages)):
            if pages[i] in rules.get(pages[j], set()):
                    return False
    return True

with open("input.txt") as f:
    rules, seqs = read_input(f)
    res = 0
    for seq in seqs:
        if is_valid(seq, rules):
            res += seq[len(seq) // 2]
    print(res)

