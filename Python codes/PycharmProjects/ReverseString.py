c=input()
class revStr:
    def func(a):
        a = a.split(' ')
        l = len(a)
        b=''
        for i in range(l):
            b = b + a[(i * (-1)) - 1] + ' '
        return(b)
print(revStr.func(c))