def main(n):
    s = str(bin(n))[2:]
    if n%2 == 0:
        s = s + str(bin(s.count('1')))[2:]
    else: s = '1' + s + '00'
    return int(s,2)

a = []
for n in range(0,10000):
    r = main(n)
    if 500 <= r <= 700:
        a.append(r)
print(len(a))
