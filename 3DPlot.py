__author__ = 'Matt'

from datetime import time
import matplotlib

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

TEMPERATURE = 1
HUMIDITY = 2
FLOW = 0
EVAPORATION_RATE = 3

class plotData3D():
    def __init__(self):
        print "Plot Data."
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection = '3d')

    def plot(self,xdata,ydata,zdata,colour):
        self.ax.scatter(xdata,ydata,zdata,c=colour)

    def setaxis(self,x,y,z):
        self.ax.set_xlabel(x)
        self.ax.set_ylabel(y)
        self.ax.set_zlabel(z)

    def show(self):
        plt.show()

class dataSummary():
    def __init__(self,file):
        self.flow  = []
        self.temp = []
        self.hum = []
        self.evap = []
        file = open(file,'r')
        line = file.readline()
        for line in file:
            bits = line.split(",")
            #  Remove the new line character on the end of the string.
            bits[-1] = bits[-1][:-1]
            #  Retrieve the necessary data from the stings.
            flow = float(bits[0])
            #  First measurement
            meanEvaporation = float(bits[3])
            meanHumidity = float(bits[4])
            meanTemperature = float(bits[5])
            self.flow.append(flow)
            self.temp.append(meanTemperature)
            self.hum.append(meanHumidity)
            self.evap.append(meanEvaporation)
            #  Second measurement
            meanEvaporation = float(bits[8])
            meanHumidity = float(bits[9])
            meanTemperature = float(bits[10])
            self.flow.append(flow)
            self.temp.append(meanTemperature)
            self.hum.append(meanHumidity)
            self.evap.append(meanEvaporation)
            #  Third measurement
            meanEvaporation = float(bits[13])
            meanHumidity = float(bits[14])
            meanTemperature = float(bits[15])
            self.flow.append(flow)
            self.temp.append(meanTemperature)
            self.hum.append(meanHumidity)
            self.evap.append(meanEvaporation)
        print self.flow
        print self.temp
        print self.hum

    def split_by_flow(self):
        self.flow0 = []
        self.flow04 = []
        self.flow06 = []
        self.flow1 = []
        zipped = zip(self.flow,self.hum,self.temp,self.evap)
        #print zipped
        for i in zipped:
            if i[0] == 0:
                self.flow0.append(i)
            if i[0] == 0.4:
                self.flow04.append(i)
            if i[0] == 0.6:
                self.flow06.append(i)
            if i[0] == 1:
                self.flow1.append(i)
        print self.flow0
        self.flow0 = zip(*self.flow0)
        self.flow04 = zip(*self.flow04)
        self.flow06 = zip(*self.flow06)
        self.flow1 = zip(*self.flow1)

    def sortByMeanEvaporation(self):
        zipped = zip(self.evap,self.hum,self.temp,self.flow)
        zipped = sorted(zipped, key=getKey)
        for i in zipped:
            print i

def getKey(item):
    return item[0]

def main():
    print "Running."
    file = "C:\\Users\\Matt\\Dropbox\\PhD\\AMOEBA 2\\Evaporations\\Data to plot.csv"
    summary = dataSummary(file)
    summary.split_by_flow()
    summary.sortByMeanEvaporation()
    #dataPlot = plotData3D()
    #dataPlot.plot(summary.flow0[3],summary.flow0[2],summary.flow0[1],"b")
    #dataPlot.plot(summary.flow04[3],summary.flow04[2],summary.flow04[1],"r")
    #dataPlot.plot(summary.flow06[3],summary.flow06[2],summary.flow06[1],"g")
    #dataPlot.plot(summary.flow1[3],summary.flow1[2],summary.flow1[1],"c")
    #dataPlot.setaxis("Evaporation rate (ml/minute)", "Humidity", "Temperature")
    #dataPlot.show()

if __name__ =="__main__":
    main()