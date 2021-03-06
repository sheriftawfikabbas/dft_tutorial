from ase import Atoms
from gpaw import GPAW
from ase.optimize import QuasiNewton

# Setting up the calculation

# Place one CO2 molecule in the center of the cell

a = 10
d = 1

CO2 = Atoms('CO2', positions=[[a/2,a/2,a/2],[a/2-d,a/2,a/2],[a/2+d,a/2,a/2]], cell=(a,a,a))

# Next, we need to create a calculator object

# The optimization calculation
# First we create the GPAW object

calc_PBE = GPAW(xc='PBE')
CO2.set_calculator(calc_PBE)

# Next, we use a relaxation procedure
# Here, the atoms will be moved small steps in search for the optimal structure until the force on each atom is less that 0.05 eV/Ang

relax = QuasiNewton(CO2)
relax.run(fmax=0.05)
CO2.get_distance(0,1)
