import re
sum = 0

with open('input.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        matches = re.findall(r"mul\(\d+,\d+\)", line)
        for match in matches:
            match = match[4:][:-1]
            part1, part2 = match.split(',')
            sum += int(part1) * int(part2)
print(sum)