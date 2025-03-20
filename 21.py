import numpy as np

import matplotlib.pyplot as plt
x = np.linspace(-20, 20, 1001)

s = np.sin(x)/x
plt.plot(x,s)
plt.show()
