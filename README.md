# ERT-sim
A geophysical python package, simulating a 2D Electrical Resistance Tomography (ERT) survey.

The package will contain all the necessesary modules to forward model DC resistivity with varying
survey geometries and geology, using analytic physical equations.

Electrode Array Types:
- Wenner, Dipole-Dipole, or Schlumberger

Resistivity Earth Models
- Homogeneous, layered, and buried sphere

Input Parameters:
- electrode current, "a" spacing, array type
- x, z, radius of buried sphere
- depth,thickness of heterogeneous layers
- resistivities of heterogenous components

Outputs:
- apparent resistivity, as a function of elecrode quadrapole midpoint
- resitivity "pseudosection"
- depth section of the geology, resistivities modelled
