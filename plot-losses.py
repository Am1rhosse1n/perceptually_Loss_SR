import matplotlib.pyplot as plt
import numpy as np
import os
a = np.load('losses_paper.npy')
b = np.load('losses_paper_NS.npy')*100
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.plot(a)
plt.plot(b)