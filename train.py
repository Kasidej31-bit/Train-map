import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



ypoints = np.array([1 , 6, 6, 6, 8, 11])

font1 = {'family':'serif','color':'blue','size':20}

plt.title("London Underground tube map", fontdict = font1)


plt.plot(ypoints, marker = 'o', ms = 10, color = 'blue')

plt.xticks([])
plt.yticks([])

plt.show()

