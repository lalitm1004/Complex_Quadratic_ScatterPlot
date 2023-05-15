import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root

def coordinate_generator(a, b, c, a_y, b_y):

    def equations(variables, A, B, C, P, Q):
        x, y = variables
        eq1 = A*(x**2 - y**2) + B*x + C - P
        eq2 = x*B + 2*x*y*A - Q
        return [eq1, eq2]

    # Initial guess for the variables x and y
    x0 = np.array([1, 1])

    # Solve the equations
    solutions = []
    solution1 = root(equations, x0, args=(a,b,c,a_y,b_y))
    if solution1.success:
        solutions.append(solution1.x)

    # Additional initial guesses for more solutions
    x0_2 = np.array([-1, -1])
    solution2 = root(equations, x0_2, args=(a,b,c,a_y,b_y))
    if solution2.success:
        solutions.append(solution2.x)


    # print(solutions)
    # print(solutions[0][0],solutions[0][1])
    # print(solutions[1][0],solutions[1][1])

    return ((solutions[0][0], solutions[0][1]), (solutions[1][0], solutions[1][1]))

fig = plt.figure()
ax = plt.axes(projection="3d")

for a_y in np.linspace(-20,20,500):
    
  coord = coordinate_generator(1,0,25,a_y,0)
  point1 = (coord[0][0], coord[0][1], a_y)
  point2 = (coord[1][0], coord[1][1], a_y)
  
  
  ax.scatter(point1[0],point1[1],point1[2], c='red')
  ax.scatter(point2[0],point2[1],point2[2], c='red')
  print(coord)
plt.show()
