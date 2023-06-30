a=input()
def pow(a):
    a=a.split(',')
    b=''
    c=''
    for i in range(1,len(a[0])):
        b=b + a[0][i]
    for i in range(len(a[1])-1):
        c=c + a[1][i]
    b=float(b)
    c=float(c)
    return(b**c)