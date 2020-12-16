from sympy import *
x = Symbol('ro')  # as ro
y = Symbol('lambda')  # as lambda
z = Symbol('mu')  # as mu
matrix = Matrix([[0, 0, 0, -1/x, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, -1/x, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, -1/x, 0, 0, 0],
                 [-(y+2*z), 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, -z, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, -z, 0, 0, 0, 0, 0, 0],
                 [-y, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [-y, 0, 0, 0, 0, 0, 0, 0, 0]])
w = matrix.eigenvals()
for key, value in w.items():
  print("{0}: {1}".format(key,value))  #Eigenvalues: multiplicity of the root