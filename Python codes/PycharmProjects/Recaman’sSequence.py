n=int(input())
a=[0]
for i in range(1, n):
    if (a[i-1] - i)>0 and (a[i-1] - i) not in a:
        a.append(a[i-1] - i)
    else:
        a.append(a[i-1] + i)

print(a)