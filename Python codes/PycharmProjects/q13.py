t=int(input())
a=[]
for i in range(t):
    a.append(int(input()))
for i in range(t):
    n=a[i]
    k=0
    sum=0
    while True:
        sum = sum + 100
        k = k + 1
        if sum >= n:
            break
        else:
            continue
        while True:
            sum = sum + 50
            k = k + 1
            if sum >= n:
                break
            else:
                continue
            while True:
                sum = sum + 10
                k = k + 1
                if sum >= n:
                    break
                else:
                    continue
                while True:
                    sum = sum + 5
                    k = k + 1
                    if sum >= n:
                        break
                    else:
                        continue
                    while True:
                        sum = sum + 2
                        k = k + 1
                        if sum >= n:
                            break
                        else:
                            continue
                        while True:
                            sum = sum + 1
                            k = k + 1
                            if sum >= n:
                                break
                            else:
                                continue
    print(k)
