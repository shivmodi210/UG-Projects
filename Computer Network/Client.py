from opcua import Client
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

url = "opc.tcp://10.185.151.135:504"
client = Client(url)
client.connect()

t = []
x_vib = []
y_vib = []
z_vib = []

def animate(i):

    Time = client.get_node("ns=2;i=5")
    Time_val = Time.get_value()
    
    Xvib = client.get_node("ns=2;i=2")
    Xvib_val = Xvib.get_value()
    
    Yvib = client.get_node("ns=2;i=3")
    Yvib_val = Yvib.get_value()
    
    Zvib = client.get_node("ns=2;i=4")
    Zvib_val = Zvib.get_value()

    t.append(Time_val)
    x_vib.append(Xvib_val)
    y_vib.append(Yvib_val)
    z_vib.append(Zvib_val)

    plt.cla()

    plt.plot(t, x_vib, label='X-axis Vibration')
    plt.plot(t, y_vib, label='Y-axis Vibration')
    plt.plot(t, z_vib, label='Z-axis Vibration')

    plt.xlabel("Time")
    plt.ylabel("Vibration")
    
    plt.legend(loc='upper right')

    plt.tight_layout()
    
    print(t, x_vib, y_vib, z_vib)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()