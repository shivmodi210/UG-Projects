t=int(input())
a=[]
o=0
e=0
for i in range(t):
    a.append(int(input()))
for i in range(t):
    if a[i]%2==0:
        e=e+1
    else:
        o=o+1
if e>o:
    print('READY')
else:
    print('NOT READY')