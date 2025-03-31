from re import findall, finditer

inp = open('3/input','r').read()

s1 = sum([int(pair[0])*int(pair[1]) for pair in findall(r'mul\((\d+),(\d+)\)', inp)])

s2, en = 0, 1
for match in finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', inp):
    inst = match.group(0)
    if inst=="do()": en = 1
    elif inst=="don't()": en = 0
    elif inst.startswith('mul(') and en:
        m1, m2 = map(int, findall(r'\d+', inst))
        s2 += m1*m2

print(s1, s2)