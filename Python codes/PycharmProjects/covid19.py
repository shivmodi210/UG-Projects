flag=0
a=str(input())
for i in range(5):
    p='1' + '0'*i + '1'
    if p in a:
        print('NO')
        flag=1
        break
if flag==0:
    print('YES')

