from collections import defaultdict
import re

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

def sort_pages(rules, pages):
    visited = set()
    result = []
    
    rule_graph = defaultdict(list)
    for x, y in rules:
        rule_graph[x].append(y)

    def sort_helper(page):
        if page in visited:
            return
        visited.add(page)
        for next_page in rule_graph[page]:
            if next_page not in visited:
                sort_helper(next_page)
        result.insert(0, page)

    for page in pages:
        if page not in visited:
            sort_helper(page)

    return result

def part2(rules, updates):
    total = 0

    for update in updates:
        print_order = get_print_order(update)
        applicable_rules = get_applicable_rules(rules, update)
        if not valid_order(print_order, applicable_rules):
            sorted_update = sort_pages(applicable_rules, update)
            total += sorted_update[len(sorted_update) // 2]

    return total

data = open("input.txt").read().strip()

rules, updates = parse(data)

result = part2(rules, updates)
print(result) 