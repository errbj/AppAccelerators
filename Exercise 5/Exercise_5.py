#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program calculates and plot the radiated energy per turn of an electron
with respec to its gamma for the Diamond Light Source.
Name: Eduardo R Rodrigues de B Jr
Date: 2020-11
To run the code just execute main().
"""

# here come the imports

import numpy as np
import matplotlib.pyplot as plt

# here come some constants all in caps, units in comments

e = 1.602E-19 #[C]
c = 3.0E8 #[m/s]
u = 1.66E-27 #[kg]
me = 9.11E-31 #[kg]
eps0 = 8.85419E-12 #[F/m]
rho_DLS = 561.6/(2*np.pi) #[m] Diamond Light Source

# here you can also define small classes, but that's another story


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
np.vectorize
def compute_gamma(m0,T):
    return T/(m0*c**2) + 1;
np.vectorize
def compute_beta(gamma):
    return np.sqrt(1 - 1/gamma**2);
np.vectorize
def compute_irr_energy(m0,q,gamma,r):
    beta = compute_beta(gamma)
    return q**2*beta**3*gamma**4/(3*eps0*r)
    

# here comes the "view", i.e. anything related to the user input/output

    # No viewers

# here comes the "controller" i.e. the manager part

def main():
    Tmax = 3.0e9 #[eV]
    Tmax = convert_ev_joule(Tmax)
    gmax = compute_gamma(me,Tmax)
    stg = (gmax - 1)/1000 #defining steps in gamma (1000 points)
    vec_gamma = np.arange(1,gmax+stg,stg)
    vec_irr = compute_irr_energy(me,e,vec_gamma,rho_DLS)
    plt.close('all')
    plt.plot(vec_gamma,vec_irr,color='b',linestyle='-',marker='')
    plt.title('Energy irradiated by an electron in DLS')
    plt.xlabel('gamma')
    plt.ylabel('Irradiated Energy (J)')
    plt.savefig('2020-11-28_irr_energy.png')
    plt.show()
   
# ------------------------
# Do not change this following part, later you will see why it isget_rigidity here:

if __name__ == '__main__':
    main()