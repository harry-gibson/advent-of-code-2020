def boot(bootcode):
    acc = 0
    visited = set()
    pos = 0

    while True:
        if pos >= len(bootcode):
            return (acc, True)
            print(pos)
            break
        if pos in visited:
            return (acc, False)
        op, n = bootcode[pos].split(' ')
        n = int(n)
        visited.add(pos)
        if op == "nop":
            pos += 1
        elif op == "acc":
            acc += n
            pos += 1
        elif op == "jmp":
            pos += n    


def swap_op(line):
    op, n = line.split(' ')
    if op == "nop": op = "jmp"
    elif op == "jmp": op = "nop"
    # leave acc unaffected
    return " ".join((op, n))
    #return "jmp" if op == "nop" else "nop"


def fix(bootcode):
    val, terminated = boot(bootcode)
    if terminated: return val, terminated
    for i, l in enumerate(bootcode):
        # don't modify the original
        code_copy = [l for l in bootcode]
        code_copy[i] = swap_op(l)
        val, terminated = boot(code_copy)
        if terminated: return val, terminated
        #bootcode[i] = swap_op(l)
    return val, False



bootcode = [r.strip() for r in open('input.txt')]

acc, term = boot(bootcode)
print(f"Part 1: the original bootcode terminates {'' if term else 'ab'}normally with accumulator value {acc}")

acc, term = fix(bootcode)
print(f"Part 2: the fixed bootcode terminates {'' if term else 'ab'}normally with accumulator value {acc}")