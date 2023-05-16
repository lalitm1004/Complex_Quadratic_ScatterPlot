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

<<<<<<< HEAD
    # print(solutions)
=======
>>>>>>> b6f858994ad5fb4c4249290afb9d5f2e595a7e08
    return ((solutions[0][0], solutions[0][1]), (solutions[1][0], solutions[1][1]))


def plot_axes():
  axis = np.linspace(-20, 20, 2000)
  zero = np.zeros_like(axis)
  
  # Plot x-axis RED
  ax.plot3D(axis, zero, zero, 'red')
  # Plot y-axis BLUE
  ax.plot3D(zero, axis, zero, 'green')
  # Plot z-axis GREEN
  ax.plot3D(zero, zero, axis, 'blue')
  ax.set_xlabel('x')
  ax.set_zlabel('y')
  ax.set_ylabel('z')

fig = plt.figure()
ax = plt.axes(projection="3d")
for b_y in np.linspace(-20,20,50):
    
    plt.cla()
    plot_axes()
    
    for a_y in np.linspace(-20,20,20):
        
        coord = coordinate_generator(1,0,9,a_y,b_y)
        point1 = (coord[0][0], coord[0][1], a_y)
        point2 = (coord[1][0], coord[1][1], a_y)
        
        
        ax.scatter(point1[0],point1[1],point1[2], c='black')
        ax.scatter(point2[0],point2[1],point2[2], c='black')
        print(coord)

    # Create a dummy line for the legend
    dummy_line = ax.plot3D([], [], [], label=f'Complex Y = {round(b_y, ndigits=2)}')
    ax.legend()

    
    plt.savefig(f'scatterplot{round(b_y, ndigits=2) + 20}.png'.replace('-','_'))