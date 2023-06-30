t=int(input())
a=[]
b=[]
for i in range(t):
    a.append(input())
    b.append(input())
for i in range(t):
    c=a[i].partition(' ')
    d=b[i]
    sum=0
    for object in range(int(c[0])):
        sum=sum+int(d[(2*object)])
    if sum>int(c[2]):
        print('NO')
    else:
        print('YES')