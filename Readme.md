# Non uniform fast fourier transform

## Introduction
This Library/Program is/was intended for use with any data Signals created by whatever Program. I've created it to analyze the Data created by Ansys Mechanical.

It is designed to be super easy to use for people with limited python knowledge, as myself.

There is a Library version and a Kivy Application, wich ist not fully working at the Moment.

## Usage
You'll need Matplotlib.pyplot, Scipy, numpy, tkinter and math to use this Library.

Say you have some 1D Signal (I'm not quite shure why it is called 1D when it is more or less 2D but thats not the point here) 

You begin with the initalization of the Class, for example:
```python
Nu = NuFFT(5000, values = ValueList, timedata = TimedataList)
```
The **5000** is the frequency in Hz to wich the Data is going to be interpolated. This can later be changed with `NuFFT.Frequenzupdate`.

**ValueList** is a List of the Y part of all the points on the graph.

**TimedataList** in a List of the X part of all the points on the graph.

___
The next step is the fourier transformation of the data and the plot output:
```python
Nu.EasyNuFFT()                      #Fourier transformation
Nu.PlotOutputOptions(log = "LogY")  #Create a Plot with Log Y scale
Nu.show()                           #Show the plot
```
You should now have a typical Matplotlib.pyplot graph on your screen.

## API
```python
NuFFT.__init__(MaxFreq, rawdata, values, timedata)
```
Initalisation of the class. All parameters are optional. If you have data diffrent to the Ansys Mechanical Layout, then import the values here.
___

```python
NuFFT.Freqencyupdate(FreqUpdate)
```
Function to change the interpolation frequency.
___

```python
NuFFT.ImportData()
```
**ANSYS SPECIFIC** This Function is used for Data only in Ansys Mechanical formated txt Data.
___

```python
NuFFT.DataConversion()
```
**ANSYS SPECIFIC** This Function is used for Data only in Ansys Mechanical formated txt Data.
___
```python
NuFFT.FFT()
```
Run the FFT on the interpolated Data. Requires that `NuFFT.Interpol()` has been run!
___
```python
NuFFT.Interpol()
```
Interpolate the given Data.
___
```python
NuFFT.PlotInput()
```
Plots the given Inputdata vs. the interpolated Values. 
TODO: label still in german...
___
```python
NuFFT.PlotOutput()
```
**depreceated** Plots a loglog and a log y subplot in a new figure. Requires `NuFFT.show()` to display an Output. 
TODO: label still in german.
___
```python
NuFFT.PlotOutputOptions(log)
```
Creates a new Figure with the NuFFT Data. log can be `linear`, `LogY`, `LogX` or `LogLog` for the axies of the plot. It defaults to `linear`. Requires `NuFFT.show()` to display an Output.
___
```python
NuFFT.show()
```
Displays the created Plots.
___
```python
NuFFT.complete()
```
**depreceated** Runs down all funtions.
____
```python
NuFFT.cleanup()
```
**depreceated** Runs `NuFFT.DataConversion()` and `NuFFT.Interpol()`
____
```python
NuFFT.ReturnOutput()
```
Returns the output of the FFT in a ziped list.
____
```python
NuFFT.easyNuFFT()
```
Runs `NuFFT.Interpol()` and `NuFFT.FFT()`


## Disclaimer
- First Problem: I'm not a professional Programmer. I've just needed an easy way to do this and thought somebody might need this too.
- Second Problem: English is not my first language. Please excuse my non optimal english.
- Third Problem: This is my first time publishing something on GitHub, so expect some weirdness :S
