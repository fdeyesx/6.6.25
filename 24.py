s = open('24 (2).txt').readline()
a = []
p = ''
for i in s:
    p += i
    if p[-1] not in '0123456789ABCDE':
        if len(p) > 1:
            a.append(p[:-1])
            p = ''
        else: p = ''
b = []
for i in range(len(a)):
    if int(a[i],15)%5 == 0:
        b.append(a[i])
print(max(b))
