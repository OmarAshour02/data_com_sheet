import numpy as np
import matplotlib.pyplot as plt

data_length = 20

x_val = np.arange(data_length)
y1 = np.random.rand(data_length)
y2 = np.random.rand(data_length)
y3 = np.random.rand(data_length)
y4 = np.random.rand(data_length)

plt.figure(figsize=(10, 8))


plt.subplot(4, 1, 1)
plt.title('First')
plt.stem(x_val, y1, label="sin(x)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 2)
plt.title('Second')
plt.stem(x_val, y2, label="sin(2 * x)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 3)
plt.title('Third')
plt.stem(x_val, y3)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 4)
plt.title('Forth')
plt.stem(x_val, y4, label="sin(6 * x)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()

plt.show()
