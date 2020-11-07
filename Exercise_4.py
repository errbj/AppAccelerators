#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program calculates the magnetic rigidity of several particles
Name: Eduardo R Rodrigues de B Jr
Date: 2020-10
To run the code just execute main().
"""

# here come the imports

import numpy as np

# here come some constants all in caps, units in comments

e = 1.602E-19 #[C]
c = 3.0E8 #[m/s]
u = 1.66E-27 #[kg]

# here you can also define small classes, but that's another story

class Particle:
    """
    This is the class particle. In the creation, the charge (multiple of e),
    mass in kg and kinetic energy in J must be given
    """""
    def __init__(self,charge,mass,kin):
        self.q = charge * e
        self.m0 = mass
        self.T = kin
        self.E = self.T + self.m0*c**2
        self.gamma = self.T/(self.m0*c**2) + 1
        self.beta = np.sqrt(1 - 1/(self.gamma*self.gamma))
    def get_rigidity(self):
        return self.beta*self.E/(abs(self.q)*c)

# here comes the "model" i.e. the computational engine, all in lower letters, with underscore, no caps
np.vectorize
def convert_ev_joule(E):
    return E*e
np.vectorize
def convert_joule_ev(E):
    return E/e
np.vectorize
def convert_u_kg(m):
    return m*u
np.vectorize
def convert_kg_u(m):
    return m/u


# here comes the "view", i.e. anything related to the user input/output

    # No viewers

# here comes the "controller" i.e. the manager part

def main():
   # 90 [AMev] 238-U-28+
   U_238 = Particle(+28,convert_u_kg(238.05),238*convert_ev_joule(90E6))
   print('Rigidity of U_238 is %0.2f [Tm]' %U_238.get_rigidity())
   # 330 [MeV/u] 197-Au-77+
   Au_197 = Particle(+77,convert_u_kg(196.97),196.97*convert_ev_joule(330E6))
   print('Rigidity of Au_197 is %0.2f [Tm]' %Au_197.get_rigidity())
   # 7 [TeV] protons
   Proton = Particle(+1,1.67E-27,convert_ev_joule(7E12))
   print('Rigidity of Proton is %0.2f [Tm]' %Proton.get_rigidity())
   # 10 [GeV] electrons
   Electron = Particle(-1,9.11E-31,convert_ev_joule(10E9))
   print('Rigidity of Electron is %0.2f [Tm]' %Electron.get_rigidity())
   
# ------------------------
# Do not change this following part, later you will see why it isget_rigidity here:

if __name__ == '__main__':
    main()