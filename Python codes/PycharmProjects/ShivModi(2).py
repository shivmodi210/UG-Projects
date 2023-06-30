import random

flag = False
rows, cols = (10, 10)
arr = [[0 for i in range(cols)] for j in range(rows)]
ar1=[1,0,0,0]
ar2=[1,1]
for i in range(23):
    ar2.append(0)

arr[5][5]=1
def process():
    for i in range(cols):
        for j in range(rows):
            if arr[i][j]==1:
                spread(i,j)
    return arr

def swapfunc():
    i=random.randrange(0,cols)
    j=random.randrange(0,rows)
    k=random.randrange(0,cols)

    if k == i:
        while True:
            l = random.randrange(0, rows)
            if l != j:
                break
    else:
        l = random.randrange(0, rows)

    m=arr[i][j]
    arr[i][j]=arr[k][l]
    arr[k][l]=m
    return arr


def spread(m, n):
    for i in range(n - 1, n + 2):
        if random.choice(ar1) == 1:
            try:
                arr[m - 1][i] = 1
            except:
                continue

        if random.choice(ar1) == 1:
            try:
                arr[m + 1][i] = 1
            except:
                continue

    for i in range(1):
        if random.choice(ar1) == 1:
            try:
                arr[m][n - 1] = 1
            except:
                continue

        if random.choice(ar1) == 1:
            try:
                arr[m][n + 1] = 1
            except:
                continue

    for i in range(n - 2, n + 3):
        if random.choice(ar2) == 1:
            try:
                arr[m - 2][i] = 1
            except:
                continue

        if random.choice(ar2) == 1:
            try:
                arr[m + 2][i] = 1
            except:
                continue

    for i in range(m - 1, m + 2):
        if random.choice(ar2) == 1:
            try:
                arr[i][n - 2] = 1
            except:
                continue

        if random.choice(ar2) == 1:
            try:
                arr[i][n + 2] = 1
            except:
                continue
    return arr


def cheak():
    for i in range(cols):
        for j in range(rows):
            if arr[i][j] == 0:
                flag = False
            else:
                flag = True
    return flag

while True:
    cheak()
    if flag==False:
        for i in range(8):
            swapfunc()
            process()
    else:
        break

print(arr)