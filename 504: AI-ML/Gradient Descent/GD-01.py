from numpy import *
from matplotlib.pyplot import *
import math
import sympy
import matplotlib.pyplot as plt

# Function 1 and its derivative
f1 = lambda x: x * x
deriv_f1 = lambda x: 2 * x
# Function 2 and its derivative
f2 = lambda x: (((sin(10 * math.pi * x)) / (2 * x)) + pow((x - 1), 4))
deriv_f2 = lambda x: -((sin(31.416 * x)) / 2 * pow(x, 1)) + ((15.708 * cos(31.416 * x)) / (x)) + (4 * pow((x - 1), 3))

errorMargin = 0.001


# l_r is the learning rate
def gradientDesc(functionName, function, deriv, low, up, x_new, x_prev, precision, l_r):
    x = linspace(low, up, 150)
    x_list, y_list = [x_new], [function(x_new)]
    while abs(x_new - x_prev) > precision:
        x_prev = x_new
        d_x = - deriv(x_prev)
        x_new = x_prev + (l_r * d_x)
        x_list.append(x_new)
        y_list.append(function(x_new))
    plt.scatter(x_list, y_list, c="g")
    plt.plot(x_list, y_list, c="b")
    plt.plot(x, function(x), c="r")
    plt.title(str(functionName) + " Gradient descent with learning rate " + str(l_r))
    plt.show()
    print("Minimum found at: (" + str(x_new) + "," + str(function(x_new)) + ")")
    print("Number of steps: " + str(len(x_list)))


# Func 1 with three learning rates
functionName = "Function 1"
print(gradientDesc(functionName, f1, deriv_f1, -5, 5, 4.5, 0, errorMargin, 0.01))
gradientDesc(functionName, f1, deriv_f1, -5, 5, 4.5, 0, errorMargin, 0.1)
gradientDesc(functionName, f1, deriv_f1, -5, 5, 4.5, 0, errorMargin, 0.9)

# Func 2 with three learning rates
functionName = "Function 2"
print(gradientDesc(functionName, f2, deriv_f2, 0.5, 2.5, 2.4, 0, errorMargin, 0.001))
gradientDesc(functionName, f2, deriv_f2, 0.5, 2.5, 2.4, 0, errorMargin, 0.005)
gradientDesc(functionName, f2, deriv_f2, 0.5, 2.5, 2.4, 0, errorMargin, 0.009)
