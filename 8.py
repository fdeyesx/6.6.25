from itertools import *
k=0
for i in product('01234567',repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        if s[0] not in '1357':
            if s[-1] not in '26':
                if s.count('7') < 3:
                    k+=1
print(k)
