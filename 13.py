from ipaddress import *
k=0
n = ip_network('214.187.224.0/255.255.224.0')
for i in n:
    f = f'{i:b}'
    if f[-4:] == '1000':
        if f.count('1')%6 != 0:
            k+=1
print(k)
