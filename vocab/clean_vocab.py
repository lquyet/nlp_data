l = []
s = set()

f_name = "vi_vocab"

with open(f_name + ".txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line in s or len(line) == 0:
            continue
        else:
            s.add(line)
            l.append(line)

with open(f_name + "_cleaned" + ".txt", "w") as f:
    f.writelines(l)


