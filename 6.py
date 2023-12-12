import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(-3.8, 3.8, 1000)

# Define the functions
y = np.cos(x_values)
y1 = 1 - (x_values**2)/2 + (x_values**4)/24


# Plot y = cos(x) (using blue color)
plt.subplot(2, 2, 1)
plt.plot(x_values, y, color='blue')
plt.title('y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')

# Plot y1 = 1 - (x^2)/2 + (x^4)/24 (using green color)
plt.subplot(2, 2, 2)
plt.plot(x_values, y1, color='green')
plt.title('y1 = 1 - (x^2)/2 + (x^4)/24')
plt.xlabel('x')
plt.ylabel('y1')

# Merge y and y1 in one figure, then draw (1) and (2) together in this merged figure
plt.subplot(2, 2, (3, 4))
plt.plot(x_values, y, label='y = cos(x)', color='blue')
plt.plot(x_values, y1, label='y1 = 1 - (x^2)/2 + (x^4)/24', color='green')
plt.title('Merged Figure - y = cos(x) and y1 = 1 - (x^2)/2 + (x^4)/24')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
