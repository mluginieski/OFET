## Program dedicated to SCLC simulations
import math

# P3HT Eg = 1.15 eV DOI:10.1021/nl0707095

e      = 1.6e-19  # [C]
epson0 = 8.85e-12 # [F/m]
k      = 1.38e-23 # [J/K]
T      = 293      # [K]
epson  = 3.0      # P3HT DOI:10.1039/C5CP03665H
mu     = 1e-6     # [m^2/Vs] DOI:10.1021/cm049617w
L      = 10.0e-6  # [m]
V      = 0.0      # [V]
Nt     = 5e20     # [m^-3] DOI:10.1103/PhysRevB.81.085305
n0     = 2.3e17   # [m^-3]
nf     = 1e21     # [m^-3] DOI:10.1103/PhysRevB.81.085305
Ef     = 5.53*e   # [J] Au Ref.: Ashcroft, N. W. and Mermin, N. D.
# P3HT HOMO = 5.03 eV; LUMO = 7.03 eV DOI:10.1126/sciadv.1701508

Et     = [5.535*e, 5.540*e, 5.545*e, 7.03*e] # [J]
dV     = 1e-1


fd = open("dados_SCLC.dat","w")

Vc = (8/9) * (e * n0 * L**2)/(epson*epson0)
print("%e " % Vc)

# Ohmic region
while V <= Vc:
    J = e * n0 * mu * V/L
    fd.write("%e %e \n" % (V,J))
    V += dV
   
# trap-SCLC region
for i in range(4):
    nt = Nt * math.exp(-(Et[i] - Ef)/(k*T))
    pt = Nt - nt
    Vtfl = (e * pt * L**2)/(epson*epson0)
    theta = nf/(nf + nt)
    print("%e %f %e %e" % (Vtfl, theta, nt, Et[i]))

    # trap-free
    if theta == 1.0:
        while V <= 310.0:
            J = 1.125 * epson * epson0 * mu *((V**2)/(L**3))
            fd.write("%e %e \n" % (V,J))
            V += dV
            
    # single trap level 
    else:
        while V < Vtfl:
            J = 1.125 * epson * epson0 * mu * theta *((V**2)/(L**3))
            fd.write("%e %e \n" % (V,J))
            V += dV
