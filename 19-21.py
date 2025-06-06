def r(n):
    if n%2 == 0: return n
    return n-1

def f(s1,s2,m):
    if s1+s2 <= 72: return m%2 == 0
    if m == 0: return 0
    h = [f(s1-3,s2,m-1),f(s1,s2-3,m-1),f(r(s1)//2,s2,m-1),f(s1,r(s2)//2,m-1)]
    return any(h) if m%2 != 0 else any(h)

print('19:', max([s for s in range(22,100) if not f(50,s,1) and f(50,s,2)]))
a = [s for s in range(22,100) if not f(50,s,1) and f(50,s,3)]
print('20:', min(a), max(a))
print('21:', max([s for s in range(22,100) if not f(50,s,1) and f(50,s,4)]))
