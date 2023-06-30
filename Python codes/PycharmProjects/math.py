def sum(a, N):
    sum=0
    for i in range(N):
        sum=sum+a[i]
    return sum

def prod(a, N):
    prod=1
    for i in range(N):
        prod=prod*a[i]
    return prod

def prime(n):
    flag=0
    for j in range(2, (n//2) + 1):
        if n%j !=0:
            continue
        else:
            flag=1
            break
    return flag