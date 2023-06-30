t=int(input())

for i in range(t):
    a=int(input())
    sum=0
    while a>0:
        sum=sum + (a%10)
        a=a//10

    print(sum)