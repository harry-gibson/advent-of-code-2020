def parse_line(line):
    nums, char, pw = line.split(' ')
    num_1, num_2 = [int(i) for i in nums.split('-')]
    char = char.strip(':')
    return num_1, num_2, char, pw

def is_valid_part1(line):
    min_occ, max_occ, char, pw = parse_line(line)
    n = pw.count(char)
    return min_occ <= n <= max_occ
    
def is_valid_part2(line):
    loc_1, loc_2, char, pw = parse_line(line)
    if max(loc_1, loc_2) > len(pw) + 1: return False
    return (pw[loc_1-1] == char) ^ (pw[loc_2-1] == char)
       

with open('input.txt') as f:
    input_lines = [l.strip() for l in f]

print (f"Part 1: {sum(map(is_valid_part1, input_lines))} passwords were valid")
print (f"Part 2: {sum(map(is_valid_part2, input_lines))} passwords were valid")