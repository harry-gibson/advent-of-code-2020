def part_one(nums, target):
    seen = set()
    possible=False
    for num in nums:
        required = target - num
        if required in seen:
            possible = True
            break
        seen.add(num)
    if possible:
        return num, required
    return -1

def part_two(nums, target):
    seen = set()
    possible = False
    for num in nums:
        for num_2 in nums:
            req_num = target - num - num_2
            if req_num in seen:
                possible = True
                break
            seen.add(num_2)
        else:
            continue
        break
    if possible:
        return num, num_2, req_num
    return -1

with open("input.txt") as input:
    nums = [int(line) for line in input]
    res = part_one(nums, 2020)
    if res != -1:
        x,y = res
        print(f"Part 1 numbers are {x}, {y}, product is {x*y}")
    else:
        print(f"Part 1 cannot be solved from this dataset")

    res_2 = part_two(nums, 2020)
    if res_2 != -1:
        x,y,z = res_2
        print(f"Part 2 numbers are {x}, {y}, {z} product is {x*y*z}")
    else:
        print(f"Part 2 cannot be solved from this dataset")