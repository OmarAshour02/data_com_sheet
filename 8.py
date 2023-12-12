import numpy as np
import matplotlib.pyplot as plt

# Parameters
f_signal = 5  # Frequency of the signal in Hertz
fs = 150  # Sampling rate in Hertz
T = 1  # Duration of the signal in seconds

# Generate time values
t_values = np.arange(0, T, 1/fs)

# Generate the signal
x = np.sin(2 * np.pi * f_signal * t_values)

# Compute the FFT
n = len(x)
freq = np.fft.fftfreq(n, d=1/fs)
fft_result = np.fft.fft(x)

# Plot the frequency domain representation
plt.plot(freq, np.abs(fft_result))
plt.title('Frequency Domain Representation')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
