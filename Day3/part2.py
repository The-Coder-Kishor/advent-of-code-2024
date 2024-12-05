import re

sum = 0

with open('input.txt', "r") as f:
    lines = f.readlines()

enabled = 1

for line in lines:
    line = line.strip()
    sections = re.split(r"don't\(\)|do\(\)", line)
    instructions = re.findall(r"don't\(\)|do\(\)", line)

    for i, section in enumerate(sections):
        if i > 0:
            if instructions[i - 1] == "do()":
                enabled = 1
            elif instructions[i - 1] == "don't()":
                enabled = 0

        matches = re.findall(r"mul\(\d+,\d+\)", section)

        if enabled:
            for match in matches:
                match = match[4:-1]
                part1, part2 = match.split(',')
                sum += int(part1) * int(part2)

print(sum)
