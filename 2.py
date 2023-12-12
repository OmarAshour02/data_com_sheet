import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 2  # Frequency in Hertz
t_values_continuous = np.arange(0, 1.1, 0.01)  # Continuous time values
t_values_discrete = np.arange(0, 1.1, 0.1)  # Discrete time values

# Continuous sine wave
continuous_signal = np.sin(2 * np.pi * f * t_values_continuous)

# Discrete sequence
discrete_signal = np.sin(2 * np.pi * f * t_values_discrete)


# Plot continuous sine wave
plt.subplot(2, 1, 1)
plt.plot(t_values_continuous, continuous_signal)
plt.title('Continuous Sine Wave - Frequency = 2Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Plot discrete sequence using stem function
plt.subplot(2, 1, 2)
plt.stem(t_values_discrete, discrete_signal)
plt.title('Discrete Sequence - Frequency = 2Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
