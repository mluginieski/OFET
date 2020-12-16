"""
    DESCRIPTION: this program calculates both characteristics curves in Organic
                 field-effect transistors: output curves and transfer curves.
                 Adapt the parameters as your need.
    OUTPUT:      two output files are generated with both output and transfer
                 data. The standard names are: output_IdxVd.dat, output_IdxVg.dat
                 
    CONTACT:     mluginieski@alunos.utfpr.edu.br
    VERSION:     20201016
"""

### Physical constants and global parameters ###
#
Ci   = 1.0e-5  # Capacitance per unit area      [F/m^2]
W    = 1.0e-3  # Width of chanel                [m]
L    = 3.0e-6  # Lenght of chanel               [m]
mu   = 2.40e-8 # Mobility of charge carriers    [m^2/Vs]
Vt   = 0.15    # Threshold voltage              [V]
dV   = 0.001   # Voltage pass                   [V]
Vmax = 0.5     # Maximum voltage to simulations [V]

### Output curves loop ###
#
fo = open("output_IdxVd.dat","w")

Vd = 0.0  # Drain voltage [V]
Vg = 0.4  # Gate voltage  [V]

while Vd <= Vmax:
    if Vd < (Vg - Vt):  # Linear regime
        Id = ((W*Ci*mu)/L)*(Vg - Vt - (Vd/2))*Vd
        
    if Vd >= (Vg - Vt): # Saturation regime
        Id = ((W*Ci*mu)/(2*L))*(Vg - Vt)**2
    
    fo.write('%.4f %e \n' % (Vd, Id))
    Vd += dV
    
fo.close()

### Transfer curves loop ###
#
fo = open("output_IdxVg.dat","w")

Vd = 0.4  # Drain voltage [V]
Vg = 0.0  # Gate voltage  [V]

while Vg <= Vmax:
    if Vd < (Vg - Vt):  # Linear regime
        Id = ((W*Ci*mu)/L)*(Vg - Vt - (Vd/2))*Vd
        
    if Vd >= (Vg - Vt): # Saturation regime
        Id = ((W*Ci*mu)/(2*L))*(Vg - Vt)**2

    fo.write('%.4f %e \n' % (Vg, Id))
    Vg += dV
    
fo.close()
