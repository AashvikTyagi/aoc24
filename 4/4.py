inp = open('4/input','r').read().splitlines()

s1 = sum([
    ''.join([inp[row+(d[0]*i)][col+(d[1]*i)] for i in range(4)]) == 'XMAS'
    for row in range(len(inp))
    for col in range(len(inp[0]))
    for d in ((-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1))
    if row+(d[0]*3) in range(len(inp)) and col+(d[1]*3) in range(len(inp[0]))
])

s2 = sum([
    set([inp[row-1][col-1],inp[row+1][col+1]])=={'M','S'}
    and set([inp[row-1][col+1],inp[row+1][col-1]])=={'M','S'}
    for row in range(len(inp))
    for col in range(len(inp[0]))
    if inp[row][col]=='A'
    if row-1 in range(len(inp)) and row+1 in range(len(inp))
    and col-1 in range(len(inp[0])) and col+1 in range(len(inp[0]))
])

print(s1, s2)
