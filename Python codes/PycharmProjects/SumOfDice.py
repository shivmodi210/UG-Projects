import random
from matplotlib import pyplot as plt
from scipy.signal import savgol_filter

List=[]

for i in range(1000):
    a=random.choice([1,2,3,4,5,6])
    b=random.choice([1,2,3,4,5,6])
    c=random.choice([1,2,3,4,5,6])
    List.append(a+b+c)

def prob(a):
    t=0
    for i in range(1000):
        if(List[i]==a):
            t=t+1
    return t/1000
x=[]
y=[]
for i in range(2, 19):
    x.append(i)
    y.append(prob(i))

#plot1

plt.bar(x, y)
plt.xlabel('Sum')
plt.ylabel('Probablity')
plt.title('Probablity of Sum of Num on Dice')
plt.xlim(1, 19)
plt.ylim(0, 0.15)
plt.show()

#plot2
yh = savgol_filter(y, 17, 2)

plt.plot(x, y, color='blue')
plt.plot(x, yh, color='red')
plt.xlabel('Sum')
plt.ylabel('Probablity')
plt.title('Probablity of Sum of Num on Dice')
plt.xlim(1, 19)
plt.ylim(0, 0.15)
plt.show()