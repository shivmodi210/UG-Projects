a=input()
def func(m):
    if len(m[0])>=len(m[2]):
        l=len(m[0])-len(m[2])
        print(' ' + m[0])
        print(m[1] + ' '*l + m[2])
        print('-'*(len(m[2])+l+1))
    else:
        l=len(m[2])-len(m[0])
        print(' '*(l+1) + m[0])
        print(m[1] + m[2])
        print('-'*(len(m[2])+1))

if '+' in a:
    b=a.partition('+')
    c= int(b[0]) + int(b[2])
    func(b)

elif '-' in a:
    b = a.partition('-')
    c = int(b[0]) - int(b[2])
    func(b)

elif '*' in a:
    b = a.partition('*')
    c = int(b[0]) * int(b[2])
    func(b)

print(c)



