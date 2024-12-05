count = 0

with open('input.txt', "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        levels = line.split()
        flag = 1
        prev_diff = 0
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
            count += 1
print(count)