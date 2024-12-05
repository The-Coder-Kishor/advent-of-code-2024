list1 = []
list2 = []
with open('input.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        part1, part2 = line.split()
        list1.append(int(part1))
        list2.append(int(part2))

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)