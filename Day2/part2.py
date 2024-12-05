count = 0

def is_safe(levels):
    prev_diff = 0
    flag = 1
    for i in range(1,len(levels)):
        diff = int(levels[i]) - int(levels[i-1])
        if abs(diff) < 1 or abs(diff) > 3:
            flag = 0
            break
        if diff * prev_diff < 0:
            flag = 0
            break
        prev_diff = diff
    if flag == 1:
        return 1
    return 0


with open('input.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        levels = line.split()
        for i in range(1, 2):
            if is_safe(levels):
                count += 1
                break
            else:
                for i in range(0, len(levels)):
                    temp = levels[i]
                    levels.pop(i)
                    if is_safe(levels):
                        count += 1
                        break
                    levels.insert(i, temp)
print(count)