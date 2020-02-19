# Non uniform fast fourier transform

## Introduction
This Library/Program is/was intended for use with any data Signals created by whatever Program. I've created it to analyze the Data created by Ansys Mechanical.

It is designed to be super easy to use for people with limited python knowledge, as myself.

There is a Library version and a Kivy Application, wich ist not fully working at the Moment.

## Usage
You'll need Matplotlib.pyplot, Scipy, numpy, tkinter and math to use this Library.

Say you have some 1D Signal (I'm not quite shure why it is called 1D when it is more or less 2D but thats not the point here) 

You begin with the initalization of the Class, for example:
```
Nu = NuFFT(5000, Data)
```
The **5000** is the frequency in Hz to wich the Data is going to be interpolated. This can later be changed with `NuFFT.Frequenzupdate`.
**Data** is an 3D Array of Raw Data separated by tabstops with a header row and an unused first column. This is how the Data is exported from Ansys. This is later going to be changed to a more usable format or there were will be an option for this.

The next step is the fourier transformation of the data and the plot output:
```
Nu.EasyNuFFT()  #Fourier transformation
Nu.PlotOutput() #Create the output plot
Nu.show()       #Show the plot
```
You should now have a typical Matplotlib.pyplot graph on your screen.

## API
## Disclaimer
First Problem: I'm not a professional Programmer. I've just needed an easy way to do this and thought somebody might need this too.
Second Problem: English is not my first language. Please excuse my non optimal english.
Third Problem: This is my first time publishing something on GitHub, so expect some weirdness :S
