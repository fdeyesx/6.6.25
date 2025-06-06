def f(n):
    s1 = ''
    while n!=0:
        s1 = str(n%7) + s1
        n //= 7
    return s1

for x in range(0,2030):
    n = 7**91 + 7**160 - x
    s = f(n)
    if s.count('0') == 70:
        print(x,s)
