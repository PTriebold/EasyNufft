import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as pyplot
import math
import tkinter as tk
from tkinter import filedialog

class DatImpo:
    def __init__(self):
        pass

    def Import(self):
        print("ImportFunc")
        explorer = tk.Tk()
        explorer.withdraw()
        rawfilepath = filedialog.askopenfile(mode="r", filetypes = (("Textdateien","*.txt"),("Alle Dateien","*.*")))
        rawfile = rawfilepath.readlines()
        explorer.destroy()
        return rawfile, rawfilepath

class NuFFT:
    def __init__(self, MaxFreq = 5000, rawdata=""):
        print("NuFFT __init__", MaxFreq, len(rawdata))
        self.maxfrequenz = MaxFreq
        self.rawfile = rawdata
    
    def Frequenzupdate(self,FreqUpdate):
        print("Frequenzupdate")
        self.maxfrequenz = FreqUpdate

    def ImportData(self):
        print("importData")
        explorer = tk.Tk()
        explorer.withdraw()
        self.rawfile = filedialog.askopenfile(mode="r", filetypes = (("Textdateien","*.txt"),("Alle Dateien","*.*"))).readlines()
        explorer.destroy()
        #return rawfile

    def DataConversion(self):
        print("DataConversion")
        #Arrays erzeugen
        self.om = [0]*(len(self.rawfile)-1)
        self.time_data = [0]*(len(self.rawfile)-1)

        #Dateikonditionierung
        for i in range(1, len(self.rawfile)):
            zeile = self.rawfile[i].split("\t")
            self.om[i-1] = float(zeile[1].replace(",","."))
            self.time_data[i-1] = float(zeile[2].replace(",","."))
        
        self.dauer = self.om[len(self.om)-1]
        self.Zeitschritt = 1/self.maxfrequenz
        
        #return om, time_data

    def FFT(self):
        print("FFT")
        fft = np.fft.fft(self.ri)
        self.fftabs = (np.absolute(fft)*2)/(len(self.ri))
        self.fftfreq2 = np.fft.fftfreq(len(self.uniformPoints),self.Zeitschritt)

    def Interpol(self):
        print("Interpol")
        self.uniformPoints = np.linspace(0,self.dauer,int(self.dauer*self.maxfrequenz))
        rbf = Rbf(self.om,self.time_data)
        self.ri = rbf(self.uniformPoints)

    def PlotInput(self):
        print("PlotInput")
        pyplot.figure()
        pyplot.plot(self.om, self.time_data,"b.",label="Eingangswerte")
        pyplot.plot(self.om, self.time_data,"b")
        pyplot.plot(self.uniformPoints,self.ri,"r",label="RBF Interpoliert")
        pyplot.xlim(0,self.dauer)
        pyplot.legend()

    def PlotOutput(self):
        print("PlotOutput")
        fig, a = pyplot.subplots(2,1)
        a[0].loglog(self.fftfreq2[:len(self.fftfreq2)//2],self.fftabs[:len(self.fftabs)//2],label="FFT des Eingangssignals")
        a[0].set_title("log log")
        a[1].semilogy(self.fftfreq2[:len(self.fftfreq2)//2],self.fftabs[:len(self.fftabs)//2],label="FFT des Eingangssignals")
        a[1].set_title("log y")
        pyplot.xlim(0,self.maxfrequenz//2)
        a[0].legend()
        a[1].legend()

    def show(self):
        print("show")
        pyplot.show()
    
    def complete(self):
        print("complete")
        self.ImportData()
        self.DataConversion()
        self.Interpol()
        self.FFT()
        self.PlotInput()
        self.PlotOutput()
        self.show()
    
    def cleanup(self):
        print("cleanup")
        self.DataConversion()
        self.Interpol()

    def ReturnOutput(self):
        output = list(zip(self.fftfreq2[:len(self.fftfreq2)//2],self.fftabs[:len(self.fftabs)//2]))
        return output

    def easyNuFFT(self):
        self.DataConversion()
        self.Interpol()
        self.FFT()


#Nu = NuFFT(5000)