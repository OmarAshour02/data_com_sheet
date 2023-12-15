import numpy as np
import matplotlib.pyplot  as plt

x_val = np.linspace(0, 10, 1000)
y1 = np.sin(x_val)
y2 = np.sin(2 * x_val)
y3 = np.sin(4 * x_val)
y4 = np.sin(6 * x_val)

plt.plot(x_val, y1, label="sin(x)")
plt.plot(x_val, y2, label="sin(2 * x)")
plt.plot(x_val, y3, label="sin(4 * x)")
plt.plot(x_val, y4, label="sin(6 * x)")

plt.title('Four Signals Together')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()


plt.show()
