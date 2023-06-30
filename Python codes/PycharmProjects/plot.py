import serial
import time
import matplotlib.pyplot as plt

plt.ion()
fig=plt.figure()

i=0
x=list()
y=list()

ser=serial.Serial('COM3', 9600)
#time.sleep(2)

ser.close()
ser.open()

while i<51:
    data=ser.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode())

    plt.scatter(i, float(data.decode()))
    #plt.plot(i, float(data.decode()))
    plt.xlabel('Time(Seconds)')
    plt.ylabel('ADC read')
    plt.title('Potentiometer Reading vs. Time')
    plt.xlim(0, 60)
    plt.ylim(0, 1100)

    i += 1
    plt.show()
    plt.pause(0.0001)