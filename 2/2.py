s1, s2 = 0, 0

def safe(lvs) -> bool:
    ordered = sorted(lvs) in (lvs, lvs[::-1])
    gradual = all([abs(lvs[i]-lvs[i+1]) in [1,2,3] for i in range(len(lvs)-1)])
    return ordered and gradual

for report in open('2/input','r').read().splitlines():
    levels = [int(level) for level in report.split()]
    s1 += safe(levels)
    s2 += any([safe(levels[:i]+levels[i+1:]) for i in range(len(levels))])

print(s1,s2)