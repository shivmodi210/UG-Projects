import math

def sp_sum(a, K, S):
    N=len(a)
    pro=math.prod(a, N)
    p=0
    for i in range(2, pro+1):
        if pro%i==0:
            f=math.prime(i)
            if f==0:
                p=p+1
    return (math.sum(a, N))*(K-(p*S))

print(sp_sum([14, 2, 7], 10, 2))