import numpy as np
import matplotlib.pyplot as plt

# Generate t values
t_values = np.arange(-20, 20, 0.01)

# Define the unit step function
unit_step_function = np.where(t_values < 0, 0, 1)

# Plot the unit step function
plt.plot(t_values, unit_step_function)
plt.title('Unit Step Function: F(x) = u(t)')
plt.xlabel('t')
plt.ylabel('F(x)')
plt.show()
