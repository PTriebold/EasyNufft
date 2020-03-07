# Non uniform fast fourier transform

## Introduction

This Library/Program is/was intended for use with any data Signals created by whatever Program. I've created it to analyze the Data created by Ansys Mechanical.

It is designed to be super easy to use for people with limited python knowledge, as myself.

There is a Library version and a Kivy Application, wich ist not fully working at the Moment.

## Usage

The fastest and imo. easiest way to interpolate some set of data is via the EasyNuFFT function:

```python
from NuFFt_Class import NuFFT

NuFFT().easyNuFFT(a,b, maxfreq=200)
```

In this case `a` is the timespace and `b` are the "measured" values. The maximum frequency we want to observe is set to 200Hz.

## Example

```python
from NuFFt_Class import NuFFT
import numpy as np
```
At first we import the two modules we need. Numpy for the generation of the data and NuFFt_Class for the analysis of said data. Since we only need a part of the NuFFt_Class module, we import only the needed class.

```python
a = np.linspace(0,3, num=2000)
b = np.sin(a*100*2*np.pi)+np.sin(a*(20*2*np.pi))+np.sin(a*(50*2*np.pi))+1
```

Here we generate a set of values compiled from three diffrent sinusoidal functions. One with a frequency of `100Hz`, one with `50Hz` and one with `20Hz`.

```python
NuFFT().easyNuFFT(a,b, maxfreq=200)
```

At last we analyse the data, by calling the `easyNuFFt` function and giving it the arguments `a` and `b` and the maximum frequency we want to observe. This function also handles the display of the Plot via `Matplotlib.pyplot`.

```python
#complete funtion

from NuFFt_Class import NuFFT
import numpy as np

a = np.linspace(0,3, num=2000)
b = np.sin(a*100*2*np.pi)+np.sin(a*(20*2*np.pi))+np.sin(a*(50*2*np.pi))+1

NuFFT().easyNuFFT(a,b, maxfreq=200)
```

## API
The API documentation can be accesed via the github internal Wiki.

## Disclaimer

- First Problem: I'm not a professional Programmer. I've just needed an easy way to do this and thought somebody might need this too.
- Second Problem: English is not my first language. Please excuse my non optimal english.
- Third Problem: This is my first time publishing something on GitHub, so expect some weirdness :S
