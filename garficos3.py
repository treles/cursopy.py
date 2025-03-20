import numpy as np

import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 100)

c0 = np.cos(x)

c1 = np.cos(x-0.2)

c2 = np.cos(x-0.4)

c3 = np.cos(x-0.6)

c4 = np.cos(x-0.8)

c5 = np.cos(x-1.0)

plt.plot(x, c0, '-')
plt.plot(x, c1, '--')
plt.plot(x, c2, ':')
plt.plot(x, c3, '-.')
plt.plot(x, c4, '.')
plt.plot(x, c5, 'o')
plt.show()
