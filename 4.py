import numpy as np
import matplotlib.pyplot  as plt

x_val = np.arange(0,10, 1000)
y1 = np.sin(x_val)
y2 = np.sin(2 * x_val)
y3 = np.sin(4 * x_val)
y4 = np.sin(6 * x_val)

plt.subplot(4,1,1)
plt.title('First')
plt.stem(x_val, y1, label="sin(x)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4,1,2)
plt.title('Second')
plt.stem(x_val, y2, label="sin(2 * x)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4,1,3)
plt.title('Third')
plt.stem(x_val, y3)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(4,1,4)
plt.title('Forth')
plt.stem(x_val, y4, label="sin(6 * x)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')



plt.tight_layout()

plt.show()
