for a in range(1,1000):
    d = set()
    for x in range(-2000,2000):
        f = ((295 <= x <= 400) <= (5 <= x < 280)) or (not(-1*a <= x <= a) <= (375 <= x <= 450))
        d.add(f)
    if False not in d:
        print(a)
