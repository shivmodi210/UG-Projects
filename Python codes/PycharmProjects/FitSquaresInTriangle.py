t=int(input())
a=[]
for i in range(t):
    a.append(int(input()))
for i in range(t):
    n=a[i]
    if n > 1:
        if n % 2 == 0:
            print((n / 4)*((n / 2) - 1))
        else:
            print((n - 1) * (n - 3) / 8)
    else:
        print('0')
