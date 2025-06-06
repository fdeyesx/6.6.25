print('a | b | c | t | f')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for t in 0,1:
                f = (not(a) or not(b)) and (not(c) or not(a)) and (t and not(a) or c and not(b))
                print(a,b,c,t,f,sep=' | ')
