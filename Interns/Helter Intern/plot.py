from tracemalloc import start
import numpy as np
import matplotlib.pyplot as plt
# import pymannkendall library
import pymannkendall as mk


def get_seasonality(data, type):
    ts_clim = data.reshape([365, -1], order='F')
    res = np.mean(ts_clim, axis=1)
    if type == 'temp':
        return np.round((res - 273.15),8)
    else:
        return res 
    
def daily_to_annual_mean(data, type):
    ts_clim = data.reshape([365, -1], order='F')
    res = np.mean(ts_clim, axis=0)
    if type == 'temp':
        return np.round((res - 273.15),8)
    else:
        return res

def plot1(data, name, xlabel, ylabel):
    fig=plt.figure()
    x = np.arange(start=1, stop=366, step=1)
    plt.plot(x, data)
    
    y_max = np.max(data)
    y_min = np.min(data)
    x_max = np.argmax(data) + 1
    x_min = np.argmin(data) + 1
    plt.annotate("max - {:.2f}".format(y_max), xy=(x_max, y_max))
    plt.annotate("min - {:.2f}".format(y_min), xy=(x_min, y_min))
    plt.xticks([1, 32, 60, 91, 121, 151, 182, 212, 243, 274, 304, 335], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    #fill in area between the two lines
    plt.fill_betweenx(np.linspace(y_min, y_max, 100), 1, 31, color='red', alpha=.3, label='Winter')  
    plt.fill_betweenx(np.linspace(y_min, y_max, 100), 274, 365, color='red', alpha=.2)    
    plt.fill_betweenx(np.linspace(y_min, y_max, 100), 32, 150, color='orange', alpha=.2, label='Summer')   
    plt.fill_betweenx(np.linspace(y_min, y_max, 100), 151, 273, color='green', alpha=.2, label='Monson')   
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(name)
    plt.legend(loc='upper left')
    plt.savefig(name + '.png',format='png')
    plt.close(fig)

def plot2(data, name, xlabel, ylabel):
    fig=plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(6)
  
    x = np.linspace(1980,2020,41)
    plt.plot(x, data, label='data')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(name)
    s = mk.original_test(data)
    y = s.slope * (x-1981) + s.intercept
    print(s)
    # plot mannkendall test result
    plt.plot(x, y ,'r', label='trend')
    plt.legend(loc='upper left')
    plt.savefig(name + '.png',format='png')
    plt.close(fig)

def plot3(temp, humidity, name, xlabel, ylabel):
    fig=plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(6)
    plt.scatter(temp, humidity, label='data')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(name)
    plt.savefig(name + '.png',format='png')
    plt.close(fig)

def plot4(temp, humidity, name, xlabel, ylabel):
    fig=plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(6)
    plt.plot(temp, humidity, label='data')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(name)
    plt.savefig(name + '.png',format='png')
    plt.close(fig)

def plot5(temp, humidity, name, y1label, y2label):
    fig, ax = plt.subplots(figsize = (10, 6))
    plt.title(name)
    
    # using the twinx() for creating another
    # axes object for secondary y-Axis
    ax2 = ax.twinx()
    ax.plot(temp, color = 'g')
    ax2.plot(humidity, color = 'b')
    
    # giving labels to the axises
    ax.set_xlabel('Day Of Year', color = 'r')
    ax.set_ylabel(y1label, color = 'g')
    
    # secondary y-axis label
    ax2.set_ylabel(y2label, color = 'b')
    
    # defining display layout
    plt.tight_layout()
    
    plt.savefig(name + '.png',format='png')
    plt.close(fig)

# load data from .npy file
relative_humidity_data = np.load('data_cities/Gandhinagar_relative_humidity.npy')
specific_humidity_data = np.load('data_cities/Gandhinagar_specific_humidity.npy')
temperature_data = np.load('data_cities/Gandhinagar_temperature.npy')

print(relative_humidity_data)
print(specific_humidity_data)
print(temperature_data)

# get seasonality
relative_humidity_seasonality = get_seasonality(relative_humidity_data, 'humidity')
specific_humidity_seasonality = get_seasonality(specific_humidity_data, 'humidity')
temperature_seasonality = get_seasonality(temperature_data, 'temp')

print("seasonality of relative humidity is: ", relative_humidity_seasonality)

print("seasonality of specific humidity is: ", specific_humidity_seasonality)

print("seasonality of temperature is: ", temperature_seasonality)

# get annual mean
relative_humidity_annual = daily_to_annual_mean(relative_humidity_data, 'humidity')
specific_humidity_annual = daily_to_annual_mean(specific_humidity_data, 'humidity')
temperature_annual = daily_to_annual_mean(temperature_data, 'temp')

print("annual mean of relative humidity is: ", relative_humidity_annual)

print("annual mean of specific humidity is: ", specific_humidity_annual)

print("annual mean of temperature is: ", temperature_annual)

# plot seasonal
plot1(relative_humidity_seasonality, "gaandhinagar_relative_humidity_seasonality", "Month", "relative humidity(%)")
plot1(specific_humidity_seasonality, "gaandhinagar_specific_humidity_seasonality", "Month", "specific humidity(g/kg)")
plot1(temperature_seasonality, "gaandhinagar_temperature_seasonality", "Month", "Temperature ($^\circ$C)")

# plot annual
plot2(relative_humidity_annual, "gaandhinagar_relative_humidity_annual", "Year", "relative humidity(%)")
plot2(specific_humidity_annual, "gaandhinagar_specific_humidity_annual", "Year", "specific humidity(g/kg)")
plot2(temperature_annual, "gaandhinagar_temperature_annual", "Year", "Temperature ($^\circ$C)")

# plot humidity vs temperature
# plot3(temperature_seasonality, specific_humidity_seasonality, "Gaandhinagar Specific humidity vs Temperature (seasonally)", "Temperature ($^\circ$C)", "specific humidity")
# plot3(temperature_annual, specific_humidity_annual, "Gaandhinagar Specific humidity vs Temperature (annual)", "Temperature ($^\circ$C)", "specific humidity")

plot5(temperature_seasonality, specific_humidity_seasonality, "Gaandhinagar Specific humidity vs Temperature (seasonality)", "Temperature ($^\circ$C)", "specific humidity")

# oh yeah, we are done
# ind = np.argsort(temperature_seasonality)
# y = specific_humidity_seasonality[ind]
# x = temperature_seasonality[ind]

# plot4(x, y, "Gaandhinagar Specific humidity vs Temperature (seasonally)", "Temperature ($^\circ$C)", "specific humidity(g/kg)")