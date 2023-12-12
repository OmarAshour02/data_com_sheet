import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
f = 10  # Frequency in Hertz
step = np.pi / 100
x_values = np.arange(0, 2 * np.pi * f, step)

# Calculate the corresponding y values
y_values = np.sin(x_values)

# Plot the sine wave
plt.plot(x_values, y_values)

# Set titles and labels
plt.title('Sine Wave - Frequency = 10Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Show the plot
plt.show()
