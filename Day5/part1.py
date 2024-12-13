def parse(data):
    rules_section, updates_section = data.split('\n\n')

    rules = []
    for line in rules_section.splitlines():
        x, y = map(int, line.split('|'))
        rules.append((x, y))

    updates = []
    for line in updates_section.splitlines():
        updates.append(list(map(int, line.split(','))))
    return rules, updates

def get_print_order(update):
    return {page: i for i, page in enumerate(update)}

def get_applicable_rules(rules, update):
    return [rule for rule in rules if rule[0] in update and rule[1] in update]

def valid_order(order, rules):
    for rule in rules:
        if order[rule[0]] > order[rule[1]]:
            return False
    return True

def part1(rules, updates):
    total = 0
    for update in updates:
        print_order = get_print_order(update)
        applicable_rules = get_applicable_rules(rules, update)
        if valid_order(print_order, applicable_rules):
            total += update[len(update) // 2]

    return total

data = open("input.txt").read().strip()

rules, updates = parse(data)

result = part1(rules, updates)

print(result)