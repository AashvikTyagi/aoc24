inp = open('input','r').read().split('\n')
l, r = [[int(q[n]) for q in [line.split('   ') for line in inp][:-1]] for n in (0,1)]
ls, rs = [sorted(s) for s in (l,r)]
s1 = sum([abs(ls[n]-rs[n]) for n in range(len(ls))])
s2 = sum([el*r.count(el) for el in l])
print(s1,s2)