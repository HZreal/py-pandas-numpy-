import numpy as np
from matplotlib import pyplot

x = np.linspace(-10, 10, 1000)
# y = x * x * x
y = np.sin(x)


pyplot.figure(figsize=(20, 8), dpi=100)
pyplot.plot(x, y)

pyplot.grid()

pyplot.show()
