import numpy as np
from kivy.app import App
from kivy.uix.button import Label, Button
from kivy.uix.widget import	Widget
from NuFFt_Class import NuFFT, DatImpo
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.graph import Graph, MeshLinePlot, Plot
from kivy.properties import ObjectProperty
from kivy.core.window import Window


abstand = 50 #Abstand zwischen den hauptlininen des Graphen
abstand_klein = 4 #Hilfslinien zwischen den Hauptlinien

class nonuniformFFT(FloatLayout):
    graph = ObjectProperty(None)


    def Oeffnen(self):
        self.Datei = DatImpo()
        self.Dat, self.Path = self.Datei.Import()
        print("Importiert")
        self.Nufft = NuFFT(rawdata=self.Dat)
        self.Nufft.DataConversion()
        print("Konvertiert")
    
    def UpdateFrequency(self):
        print("UpdateFrequency")
        self.freq = self.ids.maxfrequenztext.text
        self.Nufft.Frequenzupdate(self.freq)
        self.Analisys()

    def FFTPlot(self):
        print("FFTPlot")
        self.Analisys()
        self.points = self.Nufft.ReturnOutput()
        if self.graph.plots != []:
            self.graph.remove_plot(self.plot)
        self.graph.xmax = self.ids.maxfrequenztext.value/2
        self.plot = MeshLinePlot(color=(0,0,1,1))
        self.plot.points = self.points

        
        self.graph.add_plot(self.plot)
        print(self.graph.plots)

        #Achseneigenschaften
        #Option für Logarithmisch
    
    def Analisys(self):
        print("Analyse")
        self.freq = self.ids.maxfrequenztext.value
        self.Nufft.Frequenzupdate(self.freq)
        self.Nufft.Interpol()
        self.Nufft.FFT()

    def PlotInit(self):
        plot = MeshLinePlot(color=(0,0,1,1))
        plot.points = [(1,1),(2,2),(3,3)]
        self.graph.add_plot(plot)

    def test(self):
        #print(Window.system_size)
        #print(self.graph.size_hint[1])
        self.resize(100,100)
        #pass
    
    def resize(self, width, height):
        size_pro = self.graph.size_hint
        x_groesse = width*size_pro[0]
        #y_groesse = width*size_pro[1]
        x_spacing = self.ids.maxfrequenztext.value//(x_groesse/abstand)
        self.graph.x_ticks_major = x_spacing
        #print(graph_groesse)
        #self.graph
        #pass
        


class NuFFTkivyApp(App):
    def build(self):
        def res(Window,width,height):
            nonuniformFFT().resize(width,height)
            #pass

        Window.bind(on_resize=res)
        return nonuniformFFT()
    

if __name__ == "__main__":
    NuFFTkivyApp().run()