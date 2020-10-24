#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program reads a data file and plot the information
Name: Eduardo R Rodrigues de B Jr
Date: 2020-10
To execute the code just execute main(). The file 2016-07-11_ipm_data.txt
must be in the same directory as the Exercise_3.py file.
"""

# here come the imports

import numpy as np
import matplotlib.pyplot as plt

# here come some constants all in caps, units in comments

        # No constants

# here you can also define small classes, but that's another story

        # No classes

# here comes the "model" i.e. the computational engine, all in lower letters, with underscore, no caps

        # No models

# here comes the "view", i.e. anything related to the user input/output

def read_data_file(filename):
    print('Reading file: ' + filename)
    read_data = np.genfromtxt(filename,delimiter = '\n')
    return read_data


# here comes the "controller" i.e. the manager part


def main():
    data = read_data_file('2016-07-11_ipm_data.txt')
    posValue = np.argmax(data)
    plt.close('all')
    plt.style.use('dark_background')
    plt.plot(data,color='b',linestyle='',marker='.')
    plt.plot(posValue,data[posValue],color='r',linestyle='',marker='.')
    plt.title('IPM')
    plt.savefig('2016-07-11_ipm_data.png')
    plt.show()
    
# ------------------------
# Do not change this following part, later you will see why it is here:

if __name__ == '__main__':
    main()

