def pr(n):
    for o in range(2, int(x**0.5)+1):
        if x%o == 0:
            return False
    return True
k=0
for x in range(32_500_000, 10**10):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x%i)
    if len(d) > 2:
        d = sorted(d)
        a = []
        for i in d:
            if pr(i) == True:
                a.append(i)
        S = 0
        for i in a:
            S += int(i)
        if S != 0:
            if S%145 == 0:
                k+=1
                print(x,S)
                if k == 7:
                    break
