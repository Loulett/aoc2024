
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

def less(x, y, rules):
    if y in rules.get(x, set()):
        return True
    return False

def sort_seq(seq, rules):
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            if less(seq[j], seq[i], rules):
                seq[i], seq[j] = seq[j], seq[i]
    return seq

with open("input.txt") as f:
    rules, seqs = read_input(f)
    res = 0
    for seq in seqs:
        if not is_valid(seq, rules):
            new_seq = sort_seq(seq, rules)
            res += new_seq[len(new_seq) // 2]
    print(res)

