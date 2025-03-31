l, r = [
    [int(q[n]) for q in [line.split('   ') for line in open('1/input','r').read().split('\n')][:-1]]
    for n in (0,1)
]
lsorted, rsorted = [sorted(s) for s in (l,r)]

s1 = sum([abs(lsorted[n]-rsorted[n]) for n in range(len(lsorted))])
s2 = sum([el*r.count(el) for el in l])

print(s1, s2)