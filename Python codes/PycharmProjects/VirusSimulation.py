import random
import matplotlib.pyplot as plt

flag = True
rows, cols = (1000, 1500) 
arr = [[0 for i in range(cols)] for j in range(rows)]

arr[500][750]=1

def process(arr, cols, rows):
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==1:
                spread(arr, cols, rows, i, j)
    return arr

def swapfunc(arr, cols, rows):
    i=random.randrange(0,rows)
    j=random.randrange(0,cols)
    k=random.randrange(0,rows)
    if k==i:
        while True:
            l=random.randrange(0,cols)
            if l!=j:
                break
    else:
        l=random.randrange(0,cols)
        
    m=arr[i][j]
    arr[i][j]=arr[k][l]
    arr[k][l]=m
    return arr

def spread(arr, cols, rows, m, n):
    ar1=[1,0,0,0]
    ar2=[1,1]
    for i in range(23):
        ar2.append(0)
        
    for i in range(n-1,n+2):
        if random.choice(ar1)==1:
            try: arr[m-1][i]=1
            except: continue
        
        if random.choice(ar1)==1:
            try: arr[m+1][i]=1
            except: continue
    for i in range(1):
        if random.choice(ar1)==1:
            try: arr[m][n-1]=1
            except: continue
    
        if random.choice(ar1)==1:
            try: arr[m][n+1]=1   
            except: continue
    
    for i in range(n-2,n+3):
        if random.choice(ar2)==1:
            try: arr[m-2][i]=1
            except: continue
                
        if random.choice(ar2)==1:
            try: arr[m+2][i]=1
            except: continue
    
    for i in range(m-1,m+2):
        if random.choice(ar2)==1:
            try: arr[i][n-2]=1
            except: continue
                
        if random.choice(ar2)==1:
            try: arr[i][n+2]=1
            except: continue
    return arr

iteration=0

x=[]
y=[]
z=[]
prev_no=1

while flag:
    no=0
    for i in range(8):
        swapfunc(arr, cols, rows)
    
    process(arr, cols, rows)
    iteration+=1
        
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==1:
                no=no+1
    diff=no-prev_no
    prev_no=no
    print(diff, no)
    x.append(iteration)
    y.append(no)
    z.append(diff)
    
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==0:
                flag=True
            else: flag=False
            
#pl0t1
plt.plot(x,y,color='blue')
plt.xlabel('iteration')
plt.ylabel('no of 1s')
plt.show()

#plot2
plt.plot(x,z,color='red')
plt.xlabel('iteration')
plt.ylabel('diff of num of 1s')
plt.show()

print(z[-1])