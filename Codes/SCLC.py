
import math

"""
    DESCRIPTION: this program calculates tha currents for organic semiconductors according to Mott-Gorney and trapped space charge limited current theories.
                 Adapt the parameters as your need.
    OUTPUT:      one output file is generated with I and V datas . The standard name is: output_SCLC-IxV.dat
    CONTACT:     mluginieski@alunos.utfpr.edu.br
    VERSION:     20201016
"""

### Physical constants and global parameters ###
#
e      = 1.6e-19                             # Elemetary charge                   [C]
epson0 = 8.85e-12                            # Electric vacuum permittivity       [F/m]
k      = 1.38e-23                            # Boltzmann constant                 [J/K]
T      = 293                                 # Temperature                        [K]
epson  = 3.0                                 # Dielectric constant                [.]
mu     = 1e-6                                # Mobility of charge carriers        [cm^2/Vs]
L      = 10.0e-6                             # Lenght of device                   [m]
Nt     = 5e20                                # Density of trap states             [m^-3]
n0     = 2.3e17                              # Intrinsic density of free carriers [m^-3]
nf     = 1e21                                # Density of free charge carriers    [m^-3]
Ef     = 5.53*e                              # Fermi energy                       [J]
Et     = [5.535*e, 5.540*e, 5.545*e, 7.03*e] # Trap energies                      [J]
dV     = 1e-1                                # Pass voltage                       [V]
Vmax   = 300.0                               # Maximum voltage                    [V]

fo = open("output_SCLC-IxV.dat","w")

### Begins the calculation ###
#
Vc = (8/9) * (e * n0 * L**2)/(epson*epson0) # Critical voltage
print("%e " % Vc) # Print the value on screen (shell)

V = 0.0 # [V]

# Ohmic region
while V <= Vc:
    J = e * n0 * mu * V/L
    fo.write("%e %e \n" % (V,J))
    V += dV
   
# Trap-SCLC region
for i in range(4):
    nt = Nt * math.exp(-(Et[i] - Ef)/(k*T))
    pt = Nt - nt
    Vtfl = (e * pt * L**2)/(epson*epson0)
    theta = nf/(nf + nt)
    print("%e %f %e %e" % (Vtfl, theta, nt, Et[i])) # Print important values on screen (shell)

    # Trap-free SCLC region
    if theta == 1.0:
        while V <= Vmax:
            J = 1.125 * epson * epson0 * mu *((V**2)/(L**3))
            fo.write("%e %e \n" % (V,J))
            V += dV
            
    # single trap level 
    else:
        while V < Vtfl:
            J = 1.125 * epson * epson0 * mu * theta *((V**2)/(L**3))
            fo.write("%e %e \n" % (V,J))
            V += dV
