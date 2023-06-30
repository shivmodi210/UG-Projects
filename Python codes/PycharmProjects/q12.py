a=int(input())
a=a+1
def func(a):
    result=0
    n=a
    while n>0:
        result= result*10 + n%10
        n=n//10

    if a==result:
        return a
    else:
        return func(a+1)
print(func(a))
