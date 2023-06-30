x=int(input())
y=int(input())
s=0
p=0

if x%2==1:
    x=x-1

while (s < x) and (p < y):
    s=s+2
    p=p+1

print(p)