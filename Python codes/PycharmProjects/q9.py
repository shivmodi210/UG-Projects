a=int(input())
def func(n):
 i=0
 while n>0:
    if n%2==1:
        i=i+1
        n=n//2
    else:n=n//2
 return i

def funct(p):
 if p<=2048:
   return func(p)
 else:
    p=p-2048
    funct(p)
    return func(p) + 1

print(funct(a))