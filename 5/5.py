inp = open('5/input').read().split('\n\n')

rules = {}
[
    rules.setdefault(r[0], set()).add(r[1])
    for rule in inp[0].split()
    for r in [[int(n) for n in rule.split('|')]]
]

updates = [
    [int(page) for page in update.split(',')]
    for update in inp[1].splitlines()
]

ordered = lambda update, loc=-1: all([
    not after in update[:pagen]
    for pagen in range(len(update))
    for after in rules[update[pagen]]
]) if loc==-1 else all([
    not after in update[:loc]
    for after in rules[update[loc]]
])

s1 = sum([
    update[int((len(update)/2)-0.5)]
    for update in updates
    if ordered(update)
])

unordereds = [
    update for update in updates
    if not ordered(update)
]

s2 = 0 # yes, I am aware of how horribly innefficient this is :)
for update in unordereds:
    while not ordered(update):
        for fromloc in range(len(update)):
            for toloc in range(len(update)):
                modified = update
                modified.insert(toloc, modified.pop(fromloc))
                if ordered(modified, toloc):
                    update = modified
                    break
    s2 += update[int((len(update)/2)-0.5)]

print(s1, s2)