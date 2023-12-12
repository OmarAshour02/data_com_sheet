import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000  # Sampling frequency in Hertz
T = 1/Fs  # Sampling period
L = 1500  # Length of signal

# Time vector
t = np.arange(0, L) * T

# Generate the signal
f_t = 0.7 * np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Plot the signal in the time domain
plt.subplot(2, 1, 1)
plt.plot(t, f_t)
plt.title('Signal in Time Domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Compute the FFT
n = len(f_t)
freq = np.fft.fftfreq(n, d=T)
fft_result = np.fft.fft(f_t)

# Plot the frequency domain representation
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fft_result))
plt.title('Frequency Domain Representation')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
