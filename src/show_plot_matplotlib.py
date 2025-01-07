import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("TkAgg")

# generate random data
data = np.random.rand(10, 10)  # 10x10 random data

# display with imshow
plt.imshow(data, cmap='viridis')  # use 'viridis' color map
plt.colorbar()  # add color bar
plt.title("Test Image")
plt.show()
