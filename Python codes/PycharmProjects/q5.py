n=int(input())
a=n
while a>9:
    a=a//10
sum= (n%10) + a
print(sum)