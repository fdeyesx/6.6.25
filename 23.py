def s(n):
    s1 = str(n)
    sum1 = 0
    for i in s1:
        sum1+=int(i)
    return sum1

def f(n,e):
    if n < e: return 0
    if n == e: return 1
    return f(n-4,e)+f(n-s(n),e)

print(f(36,14)*f(14,2))
