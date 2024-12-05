list1 = []
list2 = []

freq = {}

with open('input.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        part1, part2 = line.split()
        list1.append(int(part1))
        if int(part2) not in freq:
            freq[int(part2)] = 1
        else:
            freq[int(part2)] += 1

sum = 0
for i in range(len(list1)):
    if list1[i] in freq:
        sum += list1[i] * freq[list1[i]]
    else:
        sum += 0

print(sum)