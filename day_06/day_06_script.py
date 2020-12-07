
n = 0
checkset = set()
with open('input.txt', 'r') as in_file:
    for l in in_file:
        if l.strip() == '':
            n += len(checkset)
            checkset.clear()
        else:
            checkset.update((c for c in l.strip()))
    if l.strip() != '': n += len(checkset)
print(f"Part 1: total is {n}")

checkset = set()
new_group = True
n = 0
with open('input.txt', 'r') as in_file:
    for l in in_file:
        if l.strip() == '':
            n += len(checkset)
            checkset.clear()
            new_group = True
        else:
            if new_group:
                checkset.update((c for c in l.strip()))
                new_group = False
            else:
                # must be in every person: equivalent to set intersection 
                checkset.intersection_update((c for c in l.strip()))
    if l.strip() != '': n += len(checkset)
print(f"Part 2: total is {n}")