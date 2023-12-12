import numpy as np
import matplotlib.pyplot as plt

# Parameters
f1 = 1  # Frequency for x1
f2 = 3  # Frequency for x2
t_values = np.arange(0, 1, 0.001)  # Time values

# Signals
x1 = np.sin(2 * np.pi * f1 * t_values)
x2 = np.sin(2 * np.pi * f2 * t_values)

# Plot the two signals together
plt.subplot(3, 1, 1)
plt.plot(t_values, x1, label='x1=sin(2*pi*f1*t)')
plt.plot(t_values, x2, label='x2=sin(2*pi*f2*t)')
plt.title('Two Signals Together')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Plot the summation of the two signals
plt.subplot(3, 1, 2)
plt.plot(t_values, x1 + x2, label='x1 + x2')
plt.title('Summation of the Two Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Plot the multiplication of the two signals
plt.subplot(3, 1, 3)
plt.plot(t_values, x1 * x2, label='x1 * x2')
plt.title('Multiplication of the Two Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
