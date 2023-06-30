a=int(input())
b=int(input())
c=int(input())
if b>c:
    if a>b:
        print(b)
    else:
        if a>c:print(a)
        else: print(c)
else:
    if a>c:
        print(c)
    else:
        if a>b:print(a)
        else: print(b)