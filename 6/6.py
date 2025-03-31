inp = open('6/input').read().splitlines()

ro, co = [(row,inp[row].find('^'),) for row in range(len(inp)) if '^' in inp[row]][0] 
ori = inp[ro][co]
visited = set()

while ro in range(len(inp)) and co in range(len(inp[0])):
    fnum = '^>v<'.find(ori) 
    foff = ((-1,0), (0,1), (1,0), (0,-1))[fnum] 
    if inp[ro+foff[0]][co+foff[1]] == '#': ori = '^>v<'[(fnum+1)%4]
    else: 
        ro += foff[0]
        co += foff[1]
        visited.add((ro, co))

s1 = len(visited)
s2 = None # didn't do it

print(s1, s2)