import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(0, 30.0, 0.01)
s = 1 + np.sin(t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title("Voltage / Time Line Graph")
plt.grid(True)
plt.savefig("test.png")
plt.show()