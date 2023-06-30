t=int(input())
j=0
for i in range(t):
    ci=input()
    di=ci.partition(' ')
    ai=int(di[0])
    bi=int(di[2])

    for object in range(ai,bi+1):
        flag=0
        for j in range(2, (object//2) + 1):
            if object%j !=0:
                continue
            else:
                flag=1
                break
        if flag == 0:
                print(object)
    print(' ')






