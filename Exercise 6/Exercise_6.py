#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program calculates and plot the convolution between two digital signals.
Name: Eduardo R Rodrigues de B Jr
Date: 2021-01
To run the code just execute main().
"""

# here come the imports

import numpy as np
import matplotlib.pyplot as plt

# here come some constants all in caps, units in comments


# here you can also define small classes, but that's another story


# here comes the "model" i.e. the computational engine, all in lower letters, with underscore, no caps

    
# here comes the "view", i.e. anything related to the user input/output

    # No viewers

# here comes the "controller" i.e. the manager part

def main():
    x = np.array([1,2,3])
    h = np.array([4,5,6,7])
    y = np.convolve(x,h)
    plt.close('all')
    plt.stem(y)
    plt.title('Convolution y[n] = x[n] * h[n]')
    plt.savefig('2021-01-08_convolution.png')
    plt.show()
    print("y[n] = x[n] * h[n] = ",y)
   
# ------------------------
# Do not change this following part, later you will see why it isget_rigidity here:

if __name__ == '__main__':
    main()